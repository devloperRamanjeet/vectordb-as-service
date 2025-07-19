# 🧠 Flask Backend — VectorDB-as-a-Service

## Features

- Tenant provisioning with unique instance ID
- API key + JWT token issuance
- DynamoDB metadata storage
- ENV-based config
- Unit tests with `unittest`

## 📦 Routes

| Endpoint             | Method | Description                        |
|----------------------|--------|------------------------------------|
| `/provision`         | POST   | Create tenant & instance ID        |
| `/generate-token`    | POST   | Create API key + JWT token bundle  |

## 🔧 Local Run

```bash
pip install -r requirements.txt
python app.py
