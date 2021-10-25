######
Layout
######

Layout
======
::
   .REST_WebFramework/
      core
         management.py
            package_cli_executor
               function executed when package is called from shell
            existing_cli_executor
               function executed when package is called from manage.py of
               existing project (ones created using this framework)
         managementUtilities.py
            SYS_ARGS
               Contains respective dicts for functions for cli commands.
         configuration.py
            Dynamic configuration module, which stores variables used when
            framework is running.
         http1_1.py
            getRequest
               Converts 1 raw request to usable dict, and returns parsed
               request and remaining request, to be parsed again.
            getResponse
               Converts response to transmittable bytes, or raw response.
      
      host
         server.py
            Contains server code, using sockets to send / receive requests.
         connectionManager.py
            Handles requests from one connection.
      
      http
         response.py
            HttpResponse
               To create any HttpResponse among available ones.
            HttpResponseRedirect
               To create redirection HttpResponse.
            
            And other helper functions.
      
      initiator
         project.py
            create_project
               Function to create a new project in current user directory.
               Callable when executed from direct shell mode.
            create_app
               Function to create new app under existing project.
               Callable from manage.py in existing project.
         
         project_template/
            Templates for files when creating new project.
         app_templates/
            Templates for files when creating new apps in existing project.
      
      middleware
         MiddlewareExecutor.py
            Contains MiddlewareExecutor, which takes one request,
            runs it through multiple middlewares and returns response.
         requestValidator.py
            Very 1st middleware that verifies that the request is valid before
            allowing it to be passed to other middlewares.
         pathResolver.py
            Default path resolving middleware that builds URL patterns from
            urls.py of project and passes the request to the respective view.
         defaultMiddleware.py
            Last middleware that returns default responses, when no other
            middleware in list returned response.
      
      shortcuts.py
         render
            Shortcut function to render html templates.
         redirect
            Shortcut function to create redirect response from namespaces.
      
      urls
         conf.py
            path
               Function to create path for resource / view.
            include
               Function to create path for another app.
      
      views
         decorators.py
            REST_Methods
               Decorator to check if receiving request matches allowed methods.
