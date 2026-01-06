import functions_framework
from flask import Request

@functions_framework.http
def hello_world(request: Request):
    name = request.args
    return f"Hello {name}!"    
