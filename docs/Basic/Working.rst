#######
Working
#######

Description
===========
This shows the basic working / flow of requests from various components
of REST_WebFramework.

Flow / working
==============

|  Client --connection--> Server --connection-->
|  
|  --> ConnectionManager.handleConnection [
|     
|     Client --(raw_request(s))--> ConnectionManager.handleRequests [
|        
|        --(raw_request(s))--> http1_1.getRequest -
|        
|        --(request)--> middleware.MiddlewareExecutor [
|           
|           --(request)--> middleware1 --(response or None)-->
|           
|           [if None]--(request)--> middleware2 --(response or None)-->
|           
|           --return (response)-->
|           
|        ] --(response(s))--> http1_1.getResponse --(raw_responses)-->
|        
|        --return (raw_responses)-->
|        
|     ] --(raw_responses)--> Client
|     
|     x--End-connection--x
|     
|     --return-->
|     
|  ] --wait for new connection-->
|  
|  [if KeyboardInterrupt] --EXIT->>|
