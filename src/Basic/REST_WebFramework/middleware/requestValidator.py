
from REST_WebFramework import core, http

class RequestValidator:
   def get_response_or_none (request):
      scheme = request['header']['scheme']
      method = request['header']['method']
      host = request['header']['Host']
      port = int(request['header']['Port'])
      
      if (scheme != core.configuration.SCHEME):
         return http.HttpResponse(request, status_code=403)
      
      if (method not in core.configuration.METHODS):
         return http.HttpResponse(request,
            status_code=405, methods=core.configuration.METHODS,
         )
      
      if ((host != core.configuration.SERVER_HOST)
            and (host not in core.configuration.SETTINGS.ALLOWED_HOSTS)
            and ('*' not in core.configuration.SETTINGS.ALLOWED_HOSTS)
            and (host != core.configuration.DEFAULT_HOST)
         ):
         return http.HttpResponse(request, status_code=403)
      
      if (port != core.configuration.SERVER_PORT):
         return http.HttpResponse(request, status_code=403)
      
      return None
