class DefaultMiddleware:
   def get_response_or_none (request):
      if (method == 'GET'):
         return HttpResponse(request, status_code=404)
      elif (method == 'POST'):
         return HttpResponse(request, status_code=404)
      elif (method == 'PUT'):
         return HttpResponse(request, status_code=404)
      elif (method == 'CREATE'):
         return HttpResponse(request, status_code=404)
      elif (method == 'DELETE'):
         return HttpResponse(request, status_code=404)
      elif (method == 'PATCH'):
         return HttpResponse(request, status_code=404)
      
      return HttpResponse(request, status_code=500)
