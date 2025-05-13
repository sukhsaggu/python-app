import datetime
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'name': 'Flask API',
        'version': '1.0',
        'description': 'A simple Flask API',
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname': socket.gethostname(),
        'message': 'Hello, World!!',
        'deployed_on': 'k8s'

    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'name': 'Flask API',
        'version': '1.0',
        'description': 'A simple Flask API',
        'status': 'up'

    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")



# '/api/v1/details'
# 'api/v1/healthz'