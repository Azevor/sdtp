from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstCommit():
    return "Usando framework flask! Ass.: Gildo."