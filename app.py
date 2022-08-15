from flask import Flask, jsonify
import os
import random
import string
app = Flask(__name__)
@app.route("/alive", methods=["GET"])
def alive():
    resp = jsonify({"ping": "pong"})
    return resp, 200
@app.route("/launch-vm", methods=["GET"])
def launchVM():
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    port = random.randint(2000, 4000)
    os.system('echo "port={} name=sshserver-{} opn=ssh ./launchserver.sh" > /hostpipe'.format(port, name))
    resp = jsonify({"status": "success", "command": f"ssh root@36.255.70.177 -p {port}", "password": "123456"})
    return resp, 200

@app.route("/launch-terminal", methods=["GET"])
def launchTerminal():
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    port = random.randint(5000, 6000)
    os.system('echo "port={} name=termserver-{} ./launchserver.sh" > /hostpipe'.format(port, name))
    resp = jsonify({"status": "success", "url": f"http://36.255.70.177:{port}"})
    return resp, 200

def launch(port, name):
    os.system('echo "port={} name=sshserver-{} ./launchserver.sh" > /hostpipe'.format(port, name))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)