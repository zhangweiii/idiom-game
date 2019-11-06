from flask import Flask, jsonify
from game import Game

app = Flask(__name__)


@app.route('/<string:key>')
def index(key):
    game = Game(key)
    return jsonify({"data": game.start()})
