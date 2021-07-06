# coding: utf-8
'''
Importação do flask e flask_socketio
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

'''
Instancia de Flask passado como parâmetro para o socket
'''
app = Flask(__name__)
io = SocketIO(app)

messages = []


@app.route("/")
def home():
    return render_template("chat.html")

@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg) # Armazenando histórico de mensagens
    emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)

'''
Arquivo principal (rodar a aplicação)
'''
if __name__ == "__main__":
    io.run(app, host='https://sdtp.azurewebsites.net', port='80', debug=True)
