############
Data Formats
############

Raw request
===========
Format
------
   ::
      (GET|POST|PUT|CREATE|DELETE|PATCH) /path/to/resource/ HTTP/version\\r\\n
      
      Header-key: header-value\\r\\n
      
      Header-key: header-value\\r\\n
      
      Header-key: header-value\\r\\n
      
      \\r\\n
      
      Body-(if-any)[no CRLF]

Example
-------
   ::
      GET /index/ HTTP/1.1\\r\\n
      
      Host: domain.com:port\\r\\n
      
      Accept: text/html, application/json\\r\\n
      
      Content-Type: application/x-www-form-urlencoded\\r\\n
      
      Content-Length: 23\\r\\n
      
      \\r\\n
      
      key1=value1&key2=value2

Raw response
============
Format
------
   ::
      HTTP/version status_code status\\r\\n
      
      Header-key: header-value\\r\\n
      
      Header-key: header-value\\r\\n
      
      Header-key: header-value\\r\\n
      
      \\r\\n
      
      Body-(if-any)[no CRLF]

Example
-------
   ::
      HTTP/1.1 200 OK\\r\\n
      
      Connection: close\\r\\n
      
      Content-Type: text/html\\r\\n
      
      Content-Length: 30\\r\\n
      
      \\r\\n
      
      <h1>\\r\\n
         
         This is great!\\r\\n
         
      </h1>

Parsed request
==============
Format
------
   ::
      {
         
         'request': raw_request,
         
         'header': {
            
            'method': 'GET|POST|PUT|CREATE|DELETE|PATCH',
            
            'scheme': 'http|https',
            
            'Host': 'domain.com',
            
            'Port': 9000,
            
            'path': '/path/to/resource/',
            
            'Connection': 'close',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
         },
         
         'path_splitup': [
            
            'path/,
            
            'to/',
            
            'resource/',
            
         ],
         
         'values': {
            
            'key1': 'value1',
            
            'key2': 'value2',
            
         },
         
      }

Example
-------
   ::
      {
         
         'request': raw_request,
         
         'header': {
            
            'method': 'GET',
            
            'scheme': 'http',
            
            'Host': 'domain.com',
            
            'Port': 9000,
            
            'path': '/app/index/',
            
            'Connection': 'close',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
         },
         
         'path_splitup': [
            
            'app/,
            
            'index/',
            
         ],
         
         'values': {
            
            'key1': 'value1',
            
            'key2': 'value2',
            
         },
         
      }

Parsed response
===============
Format
------
   ::
      {
         
         'request': parsed_request,
         
         'status_code': 200,
         
         'status': 'OK',
         
         'header': {
            
            'Connection': 'close',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
            'header-key': 'header-value',
            
         },
         
      }

Example
-------
   ::
      {
         
         'request': parsed_request,
         
         'status_code': 200,
         
         'status': 'OK',
         
         'header': {
            
            'Connection': 'close',
            
            'Content-Type': 'text/html',
            
            'Content-Length': 30,
            
            'data': '<h1>\r\n   This is great!\r\n</h1>',
            
         },
         
      }
