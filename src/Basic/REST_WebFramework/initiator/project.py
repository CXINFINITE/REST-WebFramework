import os
import subprocess

from REST_WebFramework import core
# from ..core import configuration

def create_project(project_name):
   project_dir = os.path.abspath(
      os.path.join(core.configuration.USER_PWD, project_name)
   )
   
   try:
      temp = os.path.abspath(project_name)
   except:
      temp = project_name
   
   if (os.path.isdir(project_dir) or os.path.isfile(project_dir)
         or os.path.exists(project_dir)
      ):
      raise ValueError (
         'initiator.project.create_project: path already exists.'
      )
   
   if (os.path.isdir(temp) or os.path.isfile(temp)
         or os.path.exists(temp)
      ):
      raise ValueError (
         'initiator.project.create_project: path in name.'
      )
   
   temp = subprocess.run(['mkdir', project_dir])
   
   core.configuration.PROJECT_DIR = project_dir
   core.configuration.PROJECT_NAME = project_name
   
   main_dir = os.path.abspath(
      os.path.join(
         project_dir, project_name
      )
   )
   temp = subprocess.run(['mkdir', main_dir])
   
   tmain_dir = os.path.abspath(
      os.path.join(
         project_dir, project_name, '__init__.py'
      )
   )
   fh = open(tmain_dir, 'w')
   fh.write('')
   fh.close()
   
   temp_dir = os.path.abspath(
      os.path.join(
         core.configuration.BASE_DIR,
         'REST_WebFramework',
         'initiator', 'project_template', 'settings.py.txt'
      )
   )
   fh = open(temp_dir, 'r')
   fc = fh.read()
   fh.close()
   
   tmain_dir = os.path.abspath(
      os.path.join(
         project_dir, project_name, 'settings.py'
      )
   )
   
   fh = open(tmain_dir, 'w')
   fh.write(fc.replace('{{PROJECT_NAME}}', project_name))
   fh.close()
   
   temp_dir = os.path.abspath(
      os.path.join(
         core.configuration.BASE_DIR,
         'REST_WebFramework',
         'initiator', 'project_template', 'urls.py.txt'
      )
   )
   fh = open(temp_dir, 'r')
   fc = fh.read()
   fh.close()
   tmain_dir = os.path.abspath(
      os.path.join(
         project_dir, project_name, 'urls.py'
      )
   )
   
   fh = open(tmain_dir, 'w')
   fh.write(fc)
   fh.close()
   
   temp_dir = os.path.abspath(
      os.path.join(
         core.configuration.BASE_DIR,
         'REST_WebFramework',
         'initiator', 'project_template', 'manage.py.txt'
      )
   )
   fh = open(temp_dir, 'r')
   fc = fh.read()
   fh.close()
   tmain_dir = os.path.abspath(
      os.path.join(
         project_dir, 'manage.py'
      )
   )
   
   fh = open(tmain_dir, 'w')
   fh.write(
      fc.replace(
         '{{FRAMEWORK_DIR}}',
         os.path.abspath(
            os.path.join(
               core.configuration.BASE_DIR,# '..',
            )
         ),
      ).replace('{{PROJECT_NAME}}', core.configuration.PROJECT_NAME)
   )
   fh.close()

def create_app (app_name):
   if (app_name == core.configuration.PROJECT_NAME):
      raise ValueError (
         'initiator.project.create_app: app_name cannot be project_name.'
      )
   
   try:
      temp = os.path.abspath(app_name)
   except:
      temp = app_name
   
   if (os.path.isdir(temp) or os.path.isfile(temp)
         or os.path.exists(temp)
      ):
      raise ValueError (
         'initiator.project.create_app: path in name.'
      )
   
   app_dir = os.path.abspath(
      os.path.join(core.configuration.PROJECT_DIR, app_name)
   )
   
   temp = subprocess.run(['mkdir', app_dir])
   
   tmain_dir = os.path.abspath(
      os.path.join(
         app_dir, 'templates',
      )
   )
   temp = subprocess.run(['mkdir', tmain_dir])
   tmain_dir = os.path.abspath(
      os.path.join(
         app_dir, 'templates', app_name
      )
   )
   temp = subprocess.run(['mkdir', tmain_dir])
   
   tmain_dir = os.path.abspath(
      os.path.join(
         app_dir, '__init__.py'
      )
   )
   fh = open(tmain_dir, 'w')
   fh.write('')
   fh.close()
   
   temp_dir = os.path.abspath(
      os.path.join(
         core.configuration.BASE_DIR,
         'REST_WebFramework',
         'initiator', 'app_template', 'urls.py.txt'
      )
   )
   fh = open(temp_dir, 'r')
   fc = fh.read()
   fh.close()
   
   tmain_dir = os.path.abspath(
      os.path.join(
         app_dir, 'urls.py'
      )
   )
   fh = open(tmain_dir, 'w')
   fh.write(
      fc.replace(
         '{{PROJECT_NAME}}',
         core.configuration.PROJECT_NAME,
      ).replace('{{APP_NAME}}', app_name)
   )
   fh.close()
   
   temp_dir = os.path.abspath(
      os.path.join(
         core.configuration.BASE_DIR,
         'REST_WebFramework',
         'initiator', 'app_template', 'views.py.txt'
      )
   )
   fh = open(temp_dir, 'r')
   fc = fh.read()
   fh.close()
   
   tmain_dir = os.path.abspath(
      os.path.join(
         app_dir, 'views.py'
      )
   )
   fh = open(tmain_dir, 'w')
   fh.write(fc.replace('{{APP_NAME}}', app_name))
   fh.close()
