import uuid

def generate_instance_id(tenant_id: str) -> str:
    return f"vectordb_{tenant_id}_{uuid.uuid4().hex[:8]}"

def generate_api_key() -> str:
    return f"sk_live_{uuid.uuid4().hex[:16]}"
