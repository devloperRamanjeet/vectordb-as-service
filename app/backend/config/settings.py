import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return {
        "AWS_REGION": os.getenv("AWS_REGION", "us-east-1"),
        "DYNAMO_TABLE": os.getenv("DYNAMO_TABLE", "TenantMetadata"),
        "TOKEN_SECRET": os.getenv("TOKEN_SECRET", "change-me-please")
    }
