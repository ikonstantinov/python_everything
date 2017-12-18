from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def add(a, b):
    "Add a and b"
    return a + b

def hello():
    return "Hello"
    
dispatcher = SoapDispatcher(
    "my_dis",
    location='http://localhost:8000',
    trace=True
)
    
dispatcher.register_function(
    'Add',
    add,
    returns={'res': int},
    args={'a': int, 'b': int}
)
    
dispatcher.register_function(
    'Hello',
    hello,
    returns={'res': str},
    args={}
)
    
print "Starting"
httpd = HTTPServer(("", 8000), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
