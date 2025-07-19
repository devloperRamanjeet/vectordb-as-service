# 🔐 API Key & Token Provisioning

## 📦 Outputs After Instance Creation

| Field         | Example Value                         | Description                        |
|---------------|----------------------------------------|------------------------------------|
| `api_key`     | `sk_live_xxxxxxxxxxx`                 | Used for request authentication    |
| `api_name`    | `acme-vdb-service`                    | Public identifier of tenant API    |
| `secret_token`| JWT or HMAC signature string           | Secure token for client usage      |
| `instance_id` | `vectordb_acme_001`                   | Internal reference ID              |
| `endpoint_url`| `https://api.vdb.com/tenant/acme`     | API endpoint base URL              |

## 🔁 Token Lifecycle

- Generated via Flask backend
- Stored securely (AWS Parameter Store or DynamoDB encrypted)
- Rotation supported via dashboard or admin console

## 🧪 Example

```json
{
  "api_key": "sk_live_23fsdf....",
  "secret_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC...",
  "instance_id": "vectordb_acme_001",
  "endpoint_url": "https://api.vdb.com/tenant/acme"
}
