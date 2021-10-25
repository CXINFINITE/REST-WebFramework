from REST_WebFramework import initiator

# from ..initiator import (
#    create_project, create_app,
# )

# from initiators.project import create_project, create_app

class Resumable:
   def newProject (project_name):
      return initiator.create_project(project_name)

class Terminating:
   def help (arg=None):
      print(
         '\nREST_WebFramework\nVersion: Basic.\n'
         + 'HELP document\n\n'
         + '   -h [-H, --help, /h, /H, /help] To print this help doc.\n\n'
         + '   -d [-D, --desc, --description, /d, /D, /desc, /description]\n'
         + '      To print project description.\n\n'
         + '   -nP [--new-project, /nP, /new-project] [project_name]\n'
         + '      To create new project in current working directory.\n'
         + '      Requires project name as argument\n\n'
      )
      exit()
   
   def description ():
      print(
         '\nREST_WebFramework\nVersion: Basic.\n'
         + 'Web framework with REST methods for educational and / or\n'
         + 'demonstration purposes only.\n'
         + 'Please, DO NOT USE in production environment\n'
         + 'or for any serious projects.\n'
         + '\nUse -h [--help, -H, /h, /H, /help] for help as:\n'
         + '$ python REST_WebFramework.py -h\n'
      )
      exit()

class EResumable:
   def newApp (app_name):
      return initiator.create_app(app_name)

class ETerminating:
   def help (arg=None):
      print(
         '\nREST_WebFramework\nVersion: Basic.\n'
         + 'HELP document\n\n'
         + '   -h [-H, --help, /h, /H, /help] To print this help doc.\n\n'
         + '   -d [-D, --desc, --description, /d, /D, /desc, /description]\n'
         + '      To print project description (REST_WebFramework).\n\n'
         + '   -nA [--new-app, /nA, /new-app] [app_name] To create new app\n'
         + '      in current project.\n'
         + '      Requires app name as argument\n'
         + '   [runserver] To start DEVELOPMENT server.\n\n'
      )
      exit()
   
   def description ():
      print(
         '\nREST_WebFramework\nVersion: Basic.\n'
         + 'Web framework with REST methods for educational and / or\n'
         + 'demonstration purposes only.\n'
         + 'Please, DO NOT USE in production environment\n'
         + 'or for any serious projects.\n'
         + '\nUse -h [--help, -H, /h, /H, /help] for help as:\n'
         + '$ python manage.py -h\n'
      )
      exit()

class SYS_ARGsKey:
   def __init__ (self, function, require_arg=None):
      self.require_arg = require_arg
      self._function = function
   
   def __call__ (self, arg=None):
      if (self.require_arg == True
            and arg == None
         ):
         raise TypeError(
            'core.managementUtilities.SYS_ARGS.RESUMABLE: '
            + 'Requires 1 positional argument.'
         )
      elif (self.require_arg == False
            and arg != None
         ):
         raise TypeError(
            'core.managementUtilities.SYS_ARGS.RESUMABLE: '
            + 'Supplied 1 positional argument, requires none.'
         )
      
      if (self.require_arg in (True, None)):
         return self._function(arg)
      else:
         return self._function()
   
class SYS_ARGS:
   # newproject, newapp, getbasepath, getprojectbasepath
   RESUMABLE = {
      '-nP': SYS_ARGsKey(Resumable.newProject, True),
      '--new-project': SYS_ARGsKey(Resumable.newProject, True),
      '/nP': SYS_ARGsKey(Resumable.newProject, True),
      '/new-project': SYS_ARGsKey(Resumable.newProject, True),
   }
   
   TERMINATING = {
      '-h': SYS_ARGsKey(Terminating.help),
      '--help': SYS_ARGsKey(Terminating.help),
      '-H': SYS_ARGsKey(Terminating.help),
      '/h': SYS_ARGsKey(Terminating.help),
      '/H': SYS_ARGsKey(Terminating.help),
      '/help': SYS_ARGsKey(Terminating.help),
      
      '-d': SYS_ARGsKey(Terminating.description, False),
      '-D': SYS_ARGsKey(Terminating.description, False),
      '--desc': SYS_ARGsKey(Terminating.description, False),
      '--description': SYS_ARGsKey(Terminating.description, False),
      '/d': SYS_ARGsKey(Terminating.description, False),
      '/D': SYS_ARGsKey(Terminating.description, False),
      '/desc': SYS_ARGsKey(Terminating.description, False),
      '/description': SYS_ARGsKey(Terminating.description, False),
   }
   
   E_RESUMABLE = {
      '-nA': SYS_ARGsKey(EResumable.newApp, True),
      '--new-app': SYS_ARGsKey(EResumable.newApp, True),
      '/nA': SYS_ARGsKey(EResumable.newApp, True),
      '/new-app': SYS_ARGsKey(EResumable.newApp, True),
   }
   
   E_TERMINATING = {
      '-h': SYS_ARGsKey(ETerminating.help),
      '--help': SYS_ARGsKey(ETerminating.help),
      '-H': SYS_ARGsKey(ETerminating.help),
      '/h': SYS_ARGsKey(ETerminating.help),
      '/H': SYS_ARGsKey(ETerminating.help),
      '/help': SYS_ARGsKey(ETerminating.help),
      
      '-d': SYS_ARGsKey(ETerminating.description, False),
      '--desc': SYS_ARGsKey(ETerminating.description, False),
      '--description': SYS_ARGsKey(ETerminating.description, False),
      '/d': SYS_ARGsKey(ETerminating.description, False),
      '/D': SYS_ARGsKey(ETerminating.description, False),
      '/desc': SYS_ARGsKey(ETerminating.description, False),
      '/description': SYS_ARGsKey(ETerminating.description, False),
   }
