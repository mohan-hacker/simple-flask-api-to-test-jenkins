from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/version')
def version():
    return jsonify(status='SUCCESS', version='1.0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)