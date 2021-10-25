import datetime

def HTTP_Response (request, status_code, status, headers):
   return {
      'request': request,
      'status_code': status_code,
      'status': status,
      'header': headers,
   }

def Http200 (request, content, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
      'data': content.strip(),
      'Content-Type': content_type,
      'Content-Length': len(content.strip()),
   }
   
   return HTTP_Response(request, 200, 'OK', headers)

def Http201 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 201, 'Created', headers)

def Http202 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 202, 'Accepted', headers)

def Http204 (request):
   headers = {
      'Connection': 'close',
   }
   
   return HTTP_Response(request, 204, 'No Content', headers)

def Http302 (request, new_path, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
      'Location': new_path.strip(),
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   else:
      headers['data'] = '<a href="{0}">Location</a>'.format(
         new_uri.strip()
      )
      headers['Content-Type'] = 'text/html'
      headers['Content-Length'] = len(headers['Content-Type'])
   
   return HTTP_Response(request, 302, 'Moved Temporarily', headers)

def Http303 (request, new_path, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
      'Location': new_path.strip(),
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   else:
      headers['data'] = '<a href="{0}">Location</a>'.format(
         new_uri.strip()
      )
      headers['Content-Type'] = 'text/html'
      headers['Content-Length'] = len(headers['Content-Type'])
   
   return HTTP_Response(request, 303, 'See Other', headers)

def Http304 (request):
   headers = {
      'Connection': 'close',
      'Date': "{0}".format(
         datetime.datetime.now().strftime("%a, %d %b %Y %X %Z")
      ),
      'Content-Location': request['headers']['path'],
      'Expires': "{0}".format(
         (
            datetime.datetime.now()
            + datetime.timedelta(days=1)
         ).strftime("%a, %d %b %Y %X %Z")
      ),
   }
   
   return HTTP_Response(request, 304, 'Not Modified', headers)

def Http403 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 403, 'Forbidden', headers)

def Http404 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 404, 'Not Found', headers)

def Http405 (request, methods, content=None, content_type='text/html'):
   if (type(methods).__name__ not in ('list', 'tuple')):
      raise TypeError('http.response.http405: Incorrect method type.')
   
   if (
         len(set(methods) - set(
            ['GET', 'POST', 'PUT', 'CREATE', 'DELETE', 'PATCH',]
         )) > 0
      ):
      raise ValueError('http.response.http405: Unknown methods supplied.')
   
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
      'Allow': ", ".join(methods),
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 405, 'Method Not Allowed', headers)

def Http411 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 411, 'Length Required', headers)

def Http414 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 414, 'Request-URI Too Long', headers)

def Http500 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 500, 'Internal Server Error', headers)

def Http501 (request, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 501, 'Not Implemented', headers)

def Http505 (request, http_versions, content=None, content_type='text/html'):
   headers = {
      'Connection': request['header'].get('Connection') or 'close',
      'HTTP-Version': ", ".join(http_versions),
   }
   
   if (content != None):
      headers['data'] = content.strip()
      headers['Content-Type'] = content_type
      headers['Content-Length'] = len(content.strip())
   
   return HTTP_Response(request, 505, 'HTTP Version Not Supported', headers)

def HttpResponse (request, content=None,
      status_code=200, content_type='text/html', url='/', methods=[],
      http_versions=[],
   ):
   if (content != None and len(content.strip()) > 2):
      content = content.strip()
   else:
      content = None
      content_type = None
   
   if (url == None):
      return HttpResponse(request, status_code=500)
   
   if (methods == None
         or (type(methods).__name__ not in ('tuple', 'list'))
         or (len(set(methods) - set(
               # configuration.METHODS
               ### PUT METHODS HERE
               ['GET', 'POST', 'PUT', 'CREATE', 'DELETE', 'PATCH',]
            )) > 0
         )
      ):
      return HttpResponse(request, status_code=500)
   
   if (http_versions== None
         or (type(http_versions).__name__ not in ('tuple', 'list'))
         or (len(set(http_versions) - set(
               ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2', 'HTTP/3',]
            )) > 0
         )
      ):
      return HttpResponse(request, status_code=500)
   
   if (status_code == 200):
      if (content == None):
         return HttpResponse(request, status_code=202)
      return Http200(request, content, content_type)
   elif (status_code == 201):
      return Http201(request, content, content_type)
   elif (status_code == 202):
      return Http202(request, content, content_type)
   elif (status_code == 204):
      return Http204(request)
   elif (status_code == 302):
      return Http302(request, url, content, content_type)
   elif (status_code == 303):
      return Http303(request, url, content, content_type)
   elif (status_code == 304):
      return Http304(request)
   elif (status_code == 403):
      return Http403(request, content, content_type)
   elif (status_code == 404):
      return Http404(request, content, content_type)
   elif (status_code == 405):
      if (len(methods) < 1):
         return HttpResponse(request, status_code=500)
      return Http405(request, methods, content, content_type)
   elif (status_code == 411):
      return Http411(request, content, content_type)
   elif (status_code == 414):
      return Http414(request, content, content_type)
   elif (status_code == 500):
      return Http500(request, content, content_type)
   elif (status_code == 501):
      return Http501(request, content, content_type)
   elif (status_code == 505):
      if (len(http_versions) < 1):
         return HttpResponse(request, status_code=500)
      return Http505(request, methods, content, content_type)

def HttpResponseRedirect (request, url, content=None, content_type='text/html'):
   if (url.find('://') != -1):
      return HttpResponse(request, url=url, status_code=302,
         content=content, content_type=content_type,
      )
   elif (url.find(':') != -1):
      return HttpResponse(request, status_code=500,
         content=content, content_type=content_type,
      )
   
   if (url in ('', '/')):
      url = '/'
   
   return HttpResponse(request, url=url, status_code=302,
      content=content, content_type=content_type,
   )
