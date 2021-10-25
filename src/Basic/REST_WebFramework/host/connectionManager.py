import socket

from REST_WebFramework import core, host, http, middleware
# from .MiddlewareExecutor import MiddlewareExecutor
# from ..http import HttpResponse

class ConnectionManager:
   def handleConnection (connection, address):
      raw_requests = b''
      
      while True:
         data = connection.recv(1024)
         if (len(data) < 1 or len(data) < 1020):
            try:
               connection.shutdown(socket.SHUT_RD)
            except:
               pass
            raw_requests += data
            break
         raw_requests += data
      
      raw_responses = ConnectionManager.handleRequests(raw_requests, address)
      
      try:
         connection.sendall(raw_responses)
      except:
         pass
      
      try:
         connection.shutdown(socket.SHUT_RDWR)
      except:
         pass
      
      try:
         connection.close()
      except:
         pass
   
   def handleRequests (raw_requests, address):
      requests = []
      responses = []
      r_requests = raw_requests
      
      while (r_requests != None and (len(r_requests) > 10)):
         for version, requestParser in core.configuration.HTTP_VERSIONS.items():
            request, r_requests, error = requestParser.getRequest(r_requests)
            
            if (request != None):
               requests.append([version, request])
            
            if (error != None):
               requests.append([version, error])
      
      for request in requests:
         response = None
         if (type(request[1]).__name__ == 'int'):
            response = HttpResponse(
               {
                  'headers' : {},
               },
               status_code=request[1],
               http_versions=core.configuration.HTTP_VERSIONS.keys(),
            )
         else:
            response = middleware.MiddlewareExecutor(request[1])
         
         responses.append([request[0], response])
      
      raw_responses = ''.encode()
      
      for response in responses:
         raw_responses += core.configuration.HTTP_VERSIONS[
            response[0]
         ].getResponse(response[1])
         
         try:
            processedResponse = True if (response[1]['request']['header'].get(
               'method'
            ) != None) else False
            
            if (processedResponse):
               print(
                  "[{0}]".format(address),
                  '"{0} {1} {2}"'.format(
                     response[1]['request']['header']['method'],
                     (response[1]['request']['header']['path'] or '/'),
                     response[1]['request']['header']['protocol_version'],
                  ),
                  response[1]['status_code'],
                  response[1]['status'],
               )
            else:
               print(
                  "[{0}]".format(address),
                  "EXX: ---NOT CAPTURED---",
                  response[1]['status_code'],
                  response[1]['status'],
               )
         except:
            print(
               "[{0}]".format(address),
               'server.ConnectionManager.handleRequests: Status print error.',
            )
      
      return raw_responses
