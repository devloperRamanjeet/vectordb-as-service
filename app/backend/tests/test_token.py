import unittest
from app import app

class TokenTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_generate_token(self):
        res = self.client.post("/api/generate-token", json={
            "tenant_id": "acme", "plan": "starter"
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn("api_key", res.json)

if __name__ == "__main__":
    unittest.main()
