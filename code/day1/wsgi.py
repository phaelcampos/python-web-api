# callable - funcao(), obj(), (lambda)(...)
# environ, callback

def application(environ, start_response):
    
    #montar o response
    status = "200 OK"
    headers = [("content-type", "text/html")]
    body = b"<strong>Hello World!!!</strong"
    start_response(status, headers)
    return [body] #precisa ser retornado como iteravel para o cgi 

"""  
if __name__ == "__main__":
    from wsgiref.simple_server import m
    ake_server
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever() """