from flask import Flask
from flask_socketio import SocketIO
from database.db import db
from routes.container_routes import container_bp
from routes.socket_routes import socket_events

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chromadb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

app.register_blueprint(container_bp)
socket_events(socketio)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
