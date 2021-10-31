import os

from REST_WebFramework import core, http
# from .core import configuration

def redirect (request, path, *args, **kwargs):
   url = None
   if (path.find('://') != -1):
      url = path
   elif (path.find(':') != -1):
      namespace, r_path = path.split(':', 1)
      n_path = ''
      matched = False
      pattern_changed = False
      url_patterns = core.configuration.URL_PATTERNS.copy()
      
      while (matched == False):
         for url_pattern in url_patterns:
            if (url_pattern['namespace'] == namespace):
               if (url_pattern['is_endpoint'] == True):
                  n_path += url_pattern['path']
                  matched = True
                  break
               elif (url_pattern['is_endpoint'] == False):
                  n_path += url_pattern['path']
                  url_patterns = url_pattern['urlpatterns']
                  pattern_changed = True
                  break
         
         if (len(r_path) > 0 and r_path.find(':') == -1):
            namespace, r_path = (r_path, '',)
         elif(len(r_path) > 0 and r_path.find(':') != -1):
            namespace, r_path = r_path.split(':', 1)
         
         if (pattern_changed == False):
            break
         elif (pattern_changed == True):
            pattern_changed = False
      
      if (matched == True):
         url = n_path
      else:
         url = None
   else:
      if (path in ('', '/',)):
         url = '/'
      else:
         url = path
   
   if (url == None):
      return http.HttpResponse(request, *args, status_code=500, **kwargs,)
   
   return http.HttpResponseRedirect(request, url, *args, **kwargs)

def render (request, template, status_code=200):
   content = None
   content_type = None
   
   template_path = os.path.abspath(
      os.path.join(
         core.configuration.PROJECT_DIR, 'templates', template,
      )
   )
   
   if (not os.path.isfile(template_path)):
      template_path = os.path.abspath(
         os.path.join(
            core.configuration.PROJECT_DIR, template.split('/', 1)[0],
            'templates', template,
         )
      )
   
   if (not os.path.isfile(template_path)):
      return http.HttpResponse(
         request, status_code=500,
      )
   
   try:
      fh = open(template_path, "r")
      content = fh.read()
      fh.close()
   except:
      return http.HttpResponse(
         request, status_code=500,
      )
   
   if (len(content) < 1):
      content = None
   else:
      content = content.strip()
      template_extension = template.split('.')[-1].lower()
      
      if (template_extension == 'html'):
         content_type = 'text/html'
      elif (template_extension == 'js'):
         content_type = 'text/javascript'
      elif (template_extension == 'json'):
         content_type = 'application/json'
      elif (template_extension == 'xml'):
         content_type = 'application/xml'
      elif (template_extension in ('txt', 'text', 'rst', 'md')):
         content_type = 'text/plain'
      else:
         content_type = 'text/plain'

   return http.HttpResponse(
      request, content, content_type=content_type, status_code=status_code,
   )
