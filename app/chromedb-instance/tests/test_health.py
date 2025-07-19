from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/healthz/")
    assert res.status_code == 200
    assert "tenant_id" in res.json()
