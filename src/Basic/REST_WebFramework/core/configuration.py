from .http1_1 import http1_1

class configuration:
   PROJECT_NAME = None
   BASE_DIR = None
   PROJECT_DIR = None

   SCHEME = 'http'

   USER_PWD = None

   SERVER_EXIT = False

   DEFAULT_SERVER_SETTINGS = {
      'MODE': 'sequential',
      'MAX_WAITING': 8,
      'MAX_PARALLEL_CONNECTIONS': 4,
   }

   DEFAULT_HOST = '127.0.0.1'
   DEFAULT_PORT = 9000

   SERVER_HOST = None
   SERVER_PORT = None

   ALLOWED_ARGS = {
      '<int>': int,
      '<str>': str,
   }

   URL_PATTERNS = []

   HTTP_VERSIONS = {
      'HTTP/1.1': http1_1, # http1_1 (object)
   }

   METHODS = [
      'GET', 'POST', 'PUT', 'CREATE', 'DELETE', 'PATCH',
   ]
