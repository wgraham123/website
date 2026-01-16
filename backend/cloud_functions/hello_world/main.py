import functions_framework
from pydantic import BaseModel, ValidationError
from flask import Request

def cors_response():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": ["Authorization", "Content-Type"],
        "Access-Control-Max-Age": "3600"
    }
    return ("", 204, headers)

class HelloRequest(BaseModel):
    name: str

@functions_framework.http
def hello_world(request: Request):

    if request.method == "OPTIONS":
        return cors_response()

    headers = {"Access-Control-Allow-Origin": "*"}

    try:
        req = HelloRequest.model_validate(request.args)
    except ValidationError as e:
        return (f"Invalid request format: {e}!", 400, headers)

    return (f"Hello {req.name}!", 200, headers)    
