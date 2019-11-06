from flask import Flask, jsonify, render_template
from game import Game

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/idiom/<string:key>')
def idiom(key):
    game = Game(key)
    return jsonify({"data": game.start()})


if __name__ == '__main__':
    app.run()
