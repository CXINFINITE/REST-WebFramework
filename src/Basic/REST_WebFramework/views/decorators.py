
from REST_WebFramework import core, http
# from ..core import configuration

def REST_Methods (methods):
   def Inner (endpoint):
      if (methods == None
            or (type(methods).__name__ not in ('tuple', 'list'))
            or (len(set(methods) - set(
                  core.configuration.METHODS
               )) > 0
            )
            or (len(methods) < 1)
         ):
         raise TypeError('views.decorators.REST_Methods: Invalid methods')
      
      def wrapper (request, *args, **kwargs):
         if (request['header']['method'] in methods):
            return endpoint(request, *args, **kwargs)
         else:
            return http.HttpResponse(request,
               status_code=405, methods=methods
            )
      return wrapper
   return Inner
