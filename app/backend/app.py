from flask import Flask
from flask_socketio import SocketIO
from database.db import db
from routes.container_routs import container_bp
from routes.socket_routes import socket_events

# 🧠 Initialize Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chromadb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔄 Initialize DB & SocketIO
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# 🔗 Register Blueprints and Socket Events
app.register_blueprint(container_bp)
socket_events(socketio)

# ✅ Optional root route for browser validation
@app.route("/", methods=["GET"])
def index():
    return "🔗 Chromadb orchestration backend is running."

# 🚀 Launch Server
if __name__ == "__main__":
    print("✅ Launching Flask backend on port 8080...")
    socketio.run(app, host="0.0.0.0", port=8080)
