## 📝 `README.md`

# Chromadb Orchestration Backend

This Flask-based backend provides dynamic container orchestration for launching, managing, and monitoring Chromadb instances on AWS ECS. It serves as a middleware layer between client applications and isolated Chromadb containers, enabling multi-tenant communication with scalable architecture.

---

## 🚀 Features

- Launch Chromadb instances as **Fargate tasks** via ECS
- Track and manage container lifecycle (launch, stop, delete)
- Assign **dynamic ports** for user isolation
- Persist metadata in a relational database
- Push real-time status updates via **WebSocket**
- Integrated with **Nginx** for client → backend → container routing



## 📦 Architecture Overview


Client ⇄ Nginx ⇄ Flask Backend ⇄ AWS ECS (chromadb-instance)
                     ↳ SQLAlchemy (User/Task mapping)
                     ↳ WebSocket (Real-time logs, errors)




## 🗂 Folder Structure


backend/
├── app.py                  # Flask + SocketIO entry point
├── config.py               # AWS & ECS config
├── requirements.txt
│
├── routes/                 # API & WebSocket routes
│   ├── container_routes.py
│   └── socket_routes.py
│
├── services/               # ECS orchestration logic
│   └── ecs_manager.py
│
├── models/                 # SQLAlchemy schemas
│   ├── user.py
│   └── container.py
│
├── database/               # DB initialization
│   └── db.py
│
└── utils/
    ├── port_allocator.py   # Assign safe ports
    └── logger.py           # Logging setup






## 🧪 API Endpoints

| Method | Endpoint                   | Description                            |
|--------|----------------------------|----------------------------------------|
| POST   | `/launch`                  | Launch a chromadb ECS task             |
| POST   | `/stop/<user_id>`          | Stop user container                    |
| DELETE | `/delete/<user_id>`        | Remove container metadata              |
| GET    | `/status/<user_id>`        | Check running status                   |

---

## ⚖️ License

MIT License © 2025 Ramanjeet

---

## 🌐 Contributors

| Name      | Role                      |
|-----------|---------------------------|
| Ramanjeet | Architect & Lead Developer |
```
