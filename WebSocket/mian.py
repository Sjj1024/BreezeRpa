from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return " 首页"


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
