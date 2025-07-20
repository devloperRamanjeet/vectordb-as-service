from database.db import db
from models.user import User
from models.container import Container
from app import app

with app.app_context():
    db.create_all()
    print("✅ Database initialized successfully.")
