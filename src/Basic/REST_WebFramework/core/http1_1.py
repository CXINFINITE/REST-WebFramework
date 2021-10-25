import re
import json

from REST_WebFramework import core

class http1_1:
   def getRequest (raw_request):
      raw_request = raw_request.decode()
      
      method, path, protocol_version = str(
         raw_request.split('\r\n', 1)[0]
      ).split(' ')
      
      if (protocol_version != 'HTTP/1.1'):
         return None, raw_request.encode(), None
      
      request = {
         'request': raw_request,
         'header': {
            'method': method,
            'protocol_version': protocol_version,
            'protocol': protocol_version.split('/', 1)[0],
            'version': protocol_version.split('/', 1)[1],
         },
         'values': {
         },
      }
      
      raw_headers, raw_body = (raw_request.split('\r\n', 1)[1]).split(
         '\r\n\r\n', 1
      )
      
      for raw_header in raw_headers.split('\r\n'):
         raw_header = raw_header.replace(' ', '')
         if (raw_header.split(':', 1)[0] in ('Path', 'path')):
            continue
         
         request['header'][raw_header.split(':', 1)[0]] = raw_header.split(
            ':', 1
         )[1]
      
      if (path.find('://') != -1):
         request['header']['scheme'] = path.split('://', 1)[0]
         if (request['header'].get('Host') == None):
            raw_embedhostport = (path.split('://', 1)[1]).split(
               '/', 1
            )[0]
            if (raw_embedhostport.find(':') != -1):
               request['header']['Host'] = raw_embedhostport.split(':', 1)[0]
               request['header']['Port'] = int(
                  raw_embedhostport.split(':', 1)[1]
               )
            else:
               request['header']['Host'] = raw_embedhostport
         if (path.split('://', 1)[1].find('/') != -1):
            request['header']['path'] = (path.split('://', 1)[1]).split(
               '/', 1
            )[1]
         else:
            request['header']['path'] = ''
      else:
         request['header']['scheme'] = 'http'
         if (path in ('', '/',)):
            request['header']['path'] = ''
         else:
            if (path.startswith('/')):
               request['header']['path'] = path[1:]
            else:
               request['header']['path'] = path
      
      if (request['header'].get('Host') == None):
         request['header']['Host'] = core.configuration.HOST
      else:
         if (request['header']['Host'].find(':') != -1):
            host, port = request['header']['Host'].split(':', 1)
            request['header']['Host'] = host
            request['header']['Port'] = port
      
      if (request['header'].get('Port') == None):
         request['header']['Port'] = core.configuration.PORT
      if (request['header'].get('Connection') == None):
         request['header']['Connection'] = 'close'
      
      if(request['header']['path'] != ''):
         request['header']['path'] = re.sub(
            '\/+', '/', request['header']['path']
         )
         if (request['header']['path'] == '/'):
            request['header']['path'] = ''
      
      if(request['header']['path'] != ''):
         if(request['header']['path'].endswith('/') == False):
            path = request['header']['path']
            
            if (path.find('?') != -1):
               path, raw_data = path.split('?', 1)
               
               for data in raw_data.split('&'):
                  request['values'][data.split('=', 1)[0]] = data.split(
                     '=', 1,
                  )[1]
            else:
               path = path + '/'
            
            request['header']['path'] = path
      
      request['path_splitup'] = [point
         for point in
         re.split('([^/]+\/)', request['header']['path'])
         if (point != None and point != '' and len(point) > 0)
      ]
      
      raw_request2 = None
      
      if (request['header'].get('Content-Type') != None
            and request['header'].get('Content-Length') != None
            and int(request['header'].get('Content-Length')) > 0
         ):
         c_len = int(request['header']['Content-Length'])
         raw_body, raw_request2 = raw_body[:c_len], raw_body[c_len:]
      elif (request['header'].get('Content-Type') != None
            and (request['header'].get('Content-Length') == None
                  or int(request['header'].get('Content-Length')) < 1
            )
         ):
         return None, None, 411
         # raise TypeError('E411: core.http1_1.requests: Content-Length invalid')
      else:
         raw_request2 = raw_body
         raw_body = None
         # raise TypeError('E204: core.http1_1.requests: No content')
      
      raw_request2 = http1_1._parseFutureRequests(raw_request2)
      
      if (raw_body != None
            and request['header']['method'] in ('POST', 'PUT', 'PATCH')
         ):
         body_parsed, error = http1_1._parseBody(
            request['header']['Content-Type'],
            raw_body,
         )
         
         if(error != None):
            return None, raw_request2, error
         
         request['header']['values'].update(
            body_parsed,
         )
      
      return request, raw_request2, None

   def _parseFutureRequests (raw_request2=None):
      if (raw_request2 != None and len(raw_request2) > 10):
         rr2_l1, rr2_l2 = raw_request2.split('\r\n', 1)
         
         while (rr2_l2.find('\r\n') != -1 and len(rr2_l1) < 11):
            rr2_l1, rr2_l2 = rr2_l2.split('\r\n', 1)
            if (len(rr2_l1) > 10):
               break
         
         if (len(rr2_l1) > 10):
            raw_request2 = rr2_l1 + '\r\n' + rr2_l2
         else:
            raw_request2 = None
      else:
         raw_request2 = None
      
      if (raw_request2 != None and raw_request2 != ''):
         raw_request2 = raw_request2.encode()
      
      return raw_request2

   def _parseBody (content_type, raw_content):
      content = {}
      
      if (content_type == 'application/x-www-form-urlencoded'):
         if (raw_content.find('&') != -1):
            for pair in raw_content.split('&'):
               if (pair.find('=') != -1):
                  content[pair.split('=', 1)[0]] = pair.split('=', 1)[1]
               else:
                  continue
                  # content[pair] = None
                  #raise TypeError('E204: core.http1_1.requests: Invalid content')
         elif (raw_content.find('=') != -1):
            content[raw_content.split('=', 1)[0]] = raw_content.split('=', 1)[1]
         else:
            content = {}
            # content[raw_content] = None
            # raise TypeError('E204: core.http1_1.requests: Invalid content')
      elif (content_type == 'application/json'):
         try:
            content = json.loads(raw_content)
         except:
            content = {}
            return content, 411
            # raise TypeError('E204: core.http1_1.requests: Invalid content')
      elif (content_type == 'text/html'):
         content = {
            'data': str(raw_content),
         }
      elif (content_type == 'text/plain'):
         content = {
            'data': str(raw_content),
         }
      
      return content, None

   def getResponse (response):
      if (response['request']['header']['protocol_version'] != 'HTTP/1.1'):
         return None
      
      raw_response = "HTTP/1.1 {0} {1}\r\n".format(
         response['status_code'], response['status'],
      )
      
      for key, value in response['header'].items():
         raw_response += "{0}: {1}\r\n".format(
            key, value,
         )
      
      raw_response += "\r\n"
      
      if (response['header'].get('data') != None):
         raw_response += "{0}".format(
            response['header']['data'],
         )
      
      return raw_response.encode()
