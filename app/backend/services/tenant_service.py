from utils.dynamo import store_metadata
from utils.secrets import generate_instance_id

def provision_tenant(tenant_id, plan):
    instance_id = generate_instance_id(tenant_id)
    item = {
        "tenant_id": tenant_id,
        "plan": plan,
        "instance_id": instance_id,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    store_metadata(item)
    return {"instance_id": instance_id}
