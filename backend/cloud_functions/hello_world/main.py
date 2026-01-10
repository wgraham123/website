import os
import json
import functions_framework
import firebase_admin
from firebase_admin import auth, credentials
from pydantic import BaseModel, ValidationError
from flask import Request

FIREBASE_SA_KEY_STR = os.environ.get('FIREBASE_SA_KEY')
if not FIREBASE_SA_KEY_STR:
    raise RuntimeError("Environment variable FIREBASE_SA_KEY is missing.")
try:
    FIREBASE_SA_KEY_DICT = json.loads(FIREBASE_SA_KEY_STR)
except json.JSONDecodeError:
    raise RuntimeError("Environment variable FIREBASE_SA_KEY is malformed.")

cred = credentials.Certificate(FIREBASE_SA_KEY_DICT)

if not firebase_admin._apps:
    firebase_admin.initialize_app(
        credential=cred,
        options={"projectId": "website-98c94"}
    )

firebaseConfig = {
    "apiKey": "AIzaSyDcwYAQoye1X4YznXtyh_-mLVTxMZWlEe0",
    "authDomain": "website-98c94.firebaseapp.com",
    "projectId": "website-98c94",
    "storageBucket": "website-98c94.firebasestorage.app",
    "messagingSenderId": "403011854830",
    "appId": "1:403011854830:web:362f78ac054e8ec0c56eff",
    "measurementId": "G-9T39V72F1V"
}



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
        print("Missing auth header")
        return ("Unauthorized", 401, headers)

    id_token = auth_header.split("Bearer ")[1]

    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
    except Exception as e:
        print(f"Invalid ID Token: {e}")
        return (f"Invalid id token: {e}", 401, headers)

    try:
        req = HelloRequest.model_validate(request.args)
    except ValidationError as e:
        return (f"Invalid request format: {e}!", 400, headers)

    return (f"Hello {req.name}! Your UID is {uid}", 200, headers)    
