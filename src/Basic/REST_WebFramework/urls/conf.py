from importlib import import_module

"""
   urlpattern = [
      {
         is_endpoint: True,
         function: function(),
         namespace: namespace,
         path: path,
         methods: methods,
      },
      {
         is_endpoint: False,
         namespace: module.app_name,
         urlpatterns: module.urlpatterns
         module: modulestring,
         path: path,
      },
   ]
   
   path (
      '/path',
      (
         namespace,
         urlpatterns,
         module,
      ),
   )
   path (
      '/path',
      view(callable),
      namespace,
      methods=[],
   )
   
   include (
      'app.urls',
      namespace,
   )
"""
def path (pathstring, view, namespace=None, methods=None):
   if (callable(view)):
      if (namespace == None):
         raise TypeError('urls.conf.path: No namespace provided')
      
      if (methods == None):
         methods = []
      elif (methods != None and len(methods) < 1):
         raise ValueError('urls.conf.path: No methods specified')
      
      return {
         'is_endpoint': True,
         'function': view,
         'namespace': namespace,
         'path': pathstring,
         'methods': methods,
      }
   elif (type(view).__name__ in ('list', 'tuple')):
      return {
         'is_endpoint': False,
         'namespace': view[0],
         'urlpatterns': view[1],
         'module': view[2],
         'path': pathstring,
      }

def include (app_path, namespace=None):
   app_module = import_module(app_path)
   app_name = app_module.app_name or namespace
   
   if (app_name == None):
      raise ValueError('urls.conf.path: No app_name')
   
   return (
      app_name,
      app_module.urlpatterns,
      app_path,
   )
