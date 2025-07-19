import jwt, time
from utils.secrets import generate_api_key, generate_instance_id

def create_token_bundle(tenant_id, plan, secret):
    api_key = generate_api_key()
    instance_id = generate_instance_id(tenant_id)

    payload = {
        "tenant_id": tenant_id,
        "plan": plan,
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400
    }

    token = jwt.encode(payload, secret, algorithm="HS256")

    return {
        "api_key": api_key,
        "secret_token": token,
        "instance_id": instance_id,
        "endpoint_url": f"https://api.vdb.com/tenant/{tenant_id}",
        "metadata": {
            "model": "all-MiniLM-L6-v2",
            "dimension": 384,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    }
