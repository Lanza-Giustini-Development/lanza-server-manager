from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

compose_file_dir = "/home/antoniolanza/palworld"

@app.route('/')
def home():
    return "Welcome to the Docker Control API!"

@app.route('/palworld/shutdown', methods=['POST'])
def docker_compose_down():
    try:
        result = subprocess.run(
            ["docker", "compose", "down"], 
            cwd=compose_file_dir, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({
            "message": "Shutdown Server successfully",
            "stdout": result.stdout,
            "stderr": result.stderr
        }), 200
    except subprocess.CalledProcessError as e:
        return jsonify({
            "message": "unable to shutdown server",
            "error": str(e),
            "stdout": e.stdout,
            "stderr": e.stderr
        }), 500

@app.route('/palworld/startup', methods=['POST'])
def docker_compose_up():
    try:
        result = subprocess.run(
            ["docker", "compose", "up","-d"], 
            cwd=compose_file_dir, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({
            "message": "started up server successfully",
            "stdout": result.stdout,
            "stderr": result.stderr
        }), 200
    except subprocess.CalledProcessError as e:
        return jsonify({
            "message": "failed to startup server",
            "error": str(e),
            "stdout": e.stdout,
            "stderr": e.stderr
        }), 500

if __name__ == '__main__':
    app.run(debug=True)