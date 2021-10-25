import re

from REST_WebFramework import core, http
# from ..core import configuration

class PathResolver:
   def get_response_or_none (request):
      builtPatterns = PathResolver._buildPattern(core.configuration.URL_PATTERNS)
      
      path = request['header']['path']
      
      if (path == ''
            and (path not in builtPatterns['paths'])
         ):
         return None
      elif (path == ''
            and (path in builtPatterns['paths'])
         ):
         epoints = [epoint[1]
            for epoint in builtPatterns['endpoints']
            if (
                  (epoint[0] == '')
                  and (
                     (request['header']['method'] in epoint[1]['methods'])
                     or (len(epoint[1]['methods']) == 0)
                  )
               )
         ]
         mpoints = [mpoint
            for mpoint in epoints
            if (len(mpoint['methods']) > 0)
         ]
         if (len(mpoints) > 0):
            return mpoints[0]['function'](request)
         else:
            return epoints[0]['function'](request)
      else:
         matchFound = False
         matchMethods = []
         
         sr_paths = request['path_splitup']
         for bPIndex in range(0, len(builtPatterns['paths'])):
            sb_paths = [sb_path
               for sb_path in
               re.split('([^/]+\/)', builtPatterns['paths'][bPIndex])
               if (sb_path != None and sb_path != '' and len(sb_path) > 0)
            ]
            
            if (len(sr_paths) == len(sb_paths)):
               # Try match path[x] with path2[x] else continue
               matched, args = PathResolver._matchSPaths(sr_paths, sb_paths)
               if (matched == True):
                  matchFound = True
                  methods = builtPatterns['endpoints'][bPIndex][1]['methods']
                  method = request['header']['method']
                  matchMethods.extend(methods)
                  
                  if ((len(methods) < 1)
                        or (method in methods)
                     ):
                     return builtPatterns['endpoints'][bPIndex][1][
                        'function'
                     ](request, *args)
               else:
                  continue
            else:
               continue
         
         if (matchFound == True):
            matchMethods = list(set(matchMethods))
            return http.HttpResponse(request,
               status_code=405, methods=matchMethods
            )
      
      return None
   
   def _matchSPaths (sr_paths, sb_paths):
      arg_types = core.configuration.ALLOWED_ARGS.copy()
      
      match = True
      args = []
      
      for r_path, b_path in zip(sr_paths, sb_paths):
         if (b_path[:-1] in arg_types.keys()):
            arg = None
            try:
               arg = arg_types[b_path[:-1]](r_path[:-1])
            except:
               match = False
               break
            args.append(arg)
            continue
         else:
            if (r_path == b_path):
               continue
            else:
               match = False
               break
      
      if (match == True):
         return (True, args)
      return (False, [])
   
   def _buildPattern(urlPatterns):
      builtPatterns = {
         'paths' : [
            # path1,
            # path2, ...
         ],
         'endpoints': [
            # [path1, endpoint],
            # [path2, endpoint], ...
         ],
      }
      
      endpoints = PathResolver._getEndPoints(urlPatterns)
      
      for endpoint in endpoints:
         builtPatterns['paths'].append(endpoint['path'])
         builtPatterns['endpoints'].append(
            [endpoint['path'], endpoint.copy()]
         )
      
      return builtPatterns
   
   def _getEndPoints (oendpoints, c_path=''):
      if (len(oendpoints) == 0):
         return []
      
      endpoints = []
      
      for point in oendpoints:
         point = point.copy()
         if (point['is_endpoint'] == True):
            point['path'] = c_path + point['path']
            endpoints.append(point)
         elif (point['is_endpoint'] == False):
            epoints = PathResolver._getEndPoints(
               point['urlpatterns'], c_path + point['path']
            )
            endpoints.extend(epoints)
      
      return endpoints
