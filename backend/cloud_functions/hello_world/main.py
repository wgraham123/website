import functions_framework
from pydantic import BaseModel, ValidationError
from flask import Request

class HelloRequest(BaseModel):
    name: str

@functions_framework.http
def hello_world(request: Request):
    try:
        req = HelloRequest.model_validate(request.args)
    except ValidationError as e:
        return f"Invalid request format: {e}!"

    return f"Hello {req.name}!"    
