import socket

from flask import Flask, jsonify, redirect
from flask_restful import Api

from onyx.resources.PlainCode import BasicCode

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return redirect('/api/heartbeat')


@app.route('/api/heartbeat')
def heartbeat():
    return jsonify(dict(host=socket.getfqdn(), status="online"))


api.add_resource(BasicCode, '/api/static')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
