import os
import sys

from pathlib import Path
from importlib import import_module

sys.path.append(
   os.path.abspath(
      Path(__file__).resolve().parent.parent.parent
   )
)

from REST_WebFramework import core
# from .managementUtilities import (SYS_ARGS)
from REST_WebFramework import host

# from core.managementUtilities import SYS_ARGS
# from host.server import Server

core.configuration.BASE_DIR = os.path.abspath(
   Path(__file__).resolve().parent.parent.parent
)
core.configuration.USER_PWD = os.getcwd()

def package_cli_executor (sys_argv):
   if (len(sys_argv) < 2):
      core.SYS_ARGS.TERMINATING['--description']()
   elif (len(sys_argv) == 2):
      if (sys_argv[-1] in core.SYS_ARGS.TERMINATING.keys()):
         core.SYS_ARGS.TERMINATING[sys_argv[-1]]()
      elif (sys_argv[-1] in core.SYS_ARGS.RESUMABLE.keys()):
         core.SYS_ARGS.RESUMABLE[sys_argv[-1]]()
      else:
         print('core.management.package_cli_executor: Unknown command.')
         core.SYS_ARGS.TERMINATING['--description']()
   else:
      if (
            len(
               set.intersection(
                  set(sys_argv[1:]),
                  set(core.SYS_ARGS.TERMINATING.keys()),
               )
            ) > 0
         ):
         sys_argv_copy = sys_argv[2:].copy()
         sys_argv_copy.append(None)
         for sys_arg, arg in zip(
               sys_argv[1:],
               sys_argv_copy,
            ):
            if (sys_arg in core.SYS_ARGS.TERMINATING.keys()):
               if ((arg in core.SYS_ARGS.TERMINATING.keys())
                     or (arg in core.SYS_ARGS.RESUMABLE.keys())
                  ):
                  core.SYS_ARGS.TERMINATING[sys_arg]()
               else:
                  core.SYS_ARGS.TERMINATING[sys_arg](arg)
            else:
               continue
      else:
         arg_running = False
         sys_argv_copy = sys_argv[2:].copy()
         sys_argv_copy.append(None)
         for sys_arg, arg in zip(
               sys_argv[1:],
               sys_argv_copy,
            ):
            if (arg_running == True):
               arg_running = False
               continue
            
            if (sys_arg in core.SYS_ARGS.RESUMABLE.keys()):
               if (arg in core.SYS_ARGS.RESUMABLE.keys()):
                  core.SYS_ARGS.RESUMABLE[sys_arg]()
               else:
                  arg_running = True
                  core.SYS_ARGS.RESUMABLE[sys_arg](arg)
            else:
               print('core.management.package_cli_executor: Unknown command.')
               core.SYS_ARGS.TERMINATING['--description']()

def existing_cli_executor (project_dir, project_settings_modulestring,
      project_name, sys_argv
   ):
   core.configuration.PROJECT_DIR = os.path.abspath(project_dir)
   core.configuration.PROJECT_NAME = project_name
   
   try:
      sys.path.append(core.configuration.PROJECT_DIR)
      core.configuration.SETTINGS = import_module(project_settings_modulestring)
   except Exception as e:
      raise Exception (
         'core.management.existing_cli_executor: SETTINGS import error'
      ) from e
   
   try:
      urlconf = import_module(
         core.configuration.SETTINGS.ROOT_URLCONF
      )
   except Exception as e:
      raise Exception (
         'core.management.existing_cli_executor: URLCONF import error'
      ) from e
   
   core.configuration.URL_PATTERNS = urlconf.urlpatterns
   
   if (len(sys_argv) < 2):
      core.SYS_ARGS.E_TERMINATING['--description']()
   elif (len(sys_argv) == 2):
      if (sys_argv[-1] == 'runserver'):
         host.Server.Server()
         try:
            host.Server.start()
         except KeyboardInterrupt:
            host.Server.stop()
            print('\nServer stopped...')
         core.configuration.SERVER_EXIT = False
         exit()
      elif (sys_argv[-1] in core.SYS_ARGS.E_TERMINATING.keys()):
         core.SYS_ARGS.E_TERMINATING[sys_argv[-1]]()
      elif (sys_argv[-1] in core.SYS_ARGS.E_RESUMABLE.keys()):
         core.SYS_ARGS.E_RESUMABLE[sys_argv[-1]]()
      else:
         print('core.management.package_cli_executor: Unknown command.')
         core.SYS_ARGS.E_TERMINATING['--description']()
   else:
      if (
            len(
               set.intersection(
                  set(sys_argv[1:]),
                  set(core.SYS_ARGS.E_TERMINATING.keys()),
               )
            ) > 0
         ):
         sys_argv_copy = sys_argv[2:].copy()
         sys_argv_copy.append(None)
         for sys_arg, arg in zip(
               sys_argv[1:],
               sys_argv_copy,
            ):
            if (sys_arg in core.SYS_ARGS.E_TERMINATING.keys()):
               if ((arg in core.SYS_ARGS.E_TERMINATING.keys())
                     or (arg in core.SYS_ARGS.E_RESUMABLE.keys())
                  ):
                  core.SYS_ARGS.E_TERMINATING[sys_arg]()
               else:
                  core.SYS_ARGS.E_TERMINATING[sys_arg](arg)
            else:
               continue
      else:
         arg_running = False
         sys_argv_copy = sys_argv[2:].copy()
         sys_argv_copy.append(None)
         for sys_arg, arg in zip(
               sys_argv[1:],
               sys_argv_copy,
            ):
            if (arg_running == True):
               arg_running = False
               continue
            
            if (sys_arg in core.SYS_ARGS.E_RESUMABLE.keys()):
               if (arg in core.SYS_ARGS.E_RESUMABLE.keys()):
                  core.SYS_ARGS.E_RESUMABLE[sys_arg]()
               else:
                  arg_running = True
                  core.SYS_ARGS.E_RESUMABLE[sys_arg](arg)
            else:
               print('core.management.package_cli_executor: Unknown command.')
               core.SYS_ARGS.E_TERMINATING['--description']()
