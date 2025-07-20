from flask_socketio import emit

def socket_events(socketio):
    @socketio.on('connect')
    def on_connect():
        emit("status", {"message": "Connected to backend"})

    @socketio.on('launch_log')
    def on_log(data):
        emit("launch_progress", {"log": data})
