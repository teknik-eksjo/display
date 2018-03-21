#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify, g
import logging
import arrow


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Something very secret and hard to guess!'


@app.route("/")
def index():
    with open('last', 'r') as f:
        last_push = arrow.get(f.readline())
    return render_template('index.html', last_push = last_push)


@app.route("/update", methods=['POST'])
def update():
    logging.debug('Received request with data {}'.format(request.json))
    with open('last', 'w') as f:
        f.write(str(arrow.utcnow()))
    return jsonify({'status': 'success'})


@app.route("/push")
def push():
    with open('last', 'r') as f:
        last_push = arrow.get(f.readline())

    return jsonify({'last_push': str(last_push)})


if __name__ == "__main__":
    app.run(debug=True)
