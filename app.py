# coding: utf-8
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)
io = SocketIO(app)
messages = []


@app.route("/")
def home():
    return render_template("index.html")


@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg) # Armazenando histórico de mensagens
    emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)

if __name__ == '__main__':
	# app.run()
	io.run(app, host='https://sdtp.azurewebsites.net', port='80', debug=True)
