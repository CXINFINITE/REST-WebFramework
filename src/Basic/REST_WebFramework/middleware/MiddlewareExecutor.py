import sys
from importlib import import_module, invalidate_caches

from REST_WebFramework import core, http
# from ..core import configuration
# from ..http import HttpResponse

invalidate_caches()

def MiddlewareExecutor (request):
   response = None
   
   for middleware in core.configuration.SETTINGS.MIDDLEWARE:
      if (type(middleware).__name__ == 'str'):
         try:
            middleware = import_module(
               middleware,
               core.configuration.PROJECT_NAME
            )
            response = middleware.get_response_or_none(request)
         except:
            response = None
            continue
      else:
         try:
            response = middleware.get_response_or_none(request)
         except:
            response = None
            continue
      if (response != None
            and (type(response).__name__ == 'dict')
            and (response['request'] == request)
         ):
         break
      else:
         response = None
   
   if (response == None):
      response = http.HttpResponse(request, status_code=500)
   
   return response
