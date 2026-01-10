import functions_framework
from firebase_admin import auth, credentials
from pydantic import BaseModel, ValidationError
from flask import Request

class HelloRequest(BaseModel):
    name: str

def cors_response():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": ["Authorization", "Content-Type"],
        "Access-Control-Max-Age": "3600"
    }
    return ("", 204, headers)

@functions_framework.http
def hello_world(request: Request):

    if request.method == "OPTIONS":
        return cors_response()

    headers = {"Access-Control-Allow-Origin": "*"}

    print(request.headers)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return ("Unauthorized", 401, headers)

    id_token = auth_header.split("Bearer ")[1]

    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
    except Exception as e:
        return (f"Invalid id token: {e}", 401, headers)

    try:
        req = HelloRequest.model_validate(request.args)
    except ValidationError as e:
        return (f"Invalid request format: {e}!", 400, headers)

    return (f"Hello {req.name}! Your UID is {uid}", 200, headers)    
