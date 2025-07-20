from flask_socketio import emit,join_room

def socket_events(socketio):
    @socketio.on("connect")
    def handle_connect():
        print("⚡ Client connected")

    @socketio.on("disconnect")
    def handle_disconnect():
        print("⚡ Client disconnected")

    @socketio.on("launch_progress")
    def handle_progress(data):
        print(f"⏳ Progress: {data}")

