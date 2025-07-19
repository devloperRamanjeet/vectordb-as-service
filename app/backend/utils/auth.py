import jwt
from flask import current_app

def validate_jwt(token: str):
    secret = current_app.config["TOKEN_SECRET"]
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
