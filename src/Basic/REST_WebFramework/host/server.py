import socket
import threading
import concurrent.futures

# from .connectionManager import ConnectionManager
from REST_WebFramework import host, core

# from ..core import configuration

class Server:
   Socket = None
   ServerMode = None
   
   def Server(
         host=core.configuration.DEFAULT_HOST,
         port=core.configuration.DEFAULT_PORT,
      ):
      Server.Socket = socket.socket(
         socket.AF_INET, socket.SOCK_STREAM,
      )
      Server.Socket.setsockopt(
         socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
      )
      Server.Socket.bind((host, port,))
      
      core.configuration.SERVER_HOST = host
      core.configuration.SERVER_PORT = port
      
      Server.Socket.listen(
         core.configuration.SETTINGS.SERVER.get('MAX_WAITING')
         or core.configuration.DEFAULT_SERVER_SETTINGS['MAX_WAITING']
      )
      
      Server.ServerMode = (
         core.configuration.SETTINGS.SERVER.get('MODE')
         or core.configuration.DEFAULT_SERVER_SETTINGS['MODE']
      )
   
   def stop ():
      core.configuration.SERVER_EXIT = True
   
   def start ():
      if (Server.Socket == None):
         raise NotImplementedError(
            'host.server.Server.start: Server not initialized!'
         )
      
      core.configuration.SERVER_EXIT = False

      Server.PrintServerStats()

      if (Server.ServerMode == 'sequential'):
         while (core.configuration.SERVER_EXIT == False):
            connection, address = Server.Socket.accept()
            host.ConnectionManager.handleConnection(connection, address)
      
      try:
         Server.Socket.shutdown(socket.SHUT_RDWR)
      except:
         pass
      
      try:
         Server.Socket.close()
      except:
         pass
      
      Server.Socket = None
      Server.ServerMode = None
   
   def PrintServerStats ():
      print(
         "\n************************************************************\n"
         + "WARNING: This is development server,\n"
         + "         NOT TO BE USED in production environment.\n\n"
         + "Developement server starting on: http://{0}:{1}/\n".format(
            core.configuration.SERVER_HOST, core.configuration.SERVER_PORT,
         )
         + "Host: {0}\nPort: {1}\n\n".format(
            core.configuration.SERVER_HOST, core.configuration.SERVER_PORT,
         )
         + "Press Ctrl+C to stop.\n\n"
         + "Server requests/responses::\n\n"
      )
