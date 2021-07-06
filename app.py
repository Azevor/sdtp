# coding: utf-8
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return ("Teste 1", 200)


app.run()
