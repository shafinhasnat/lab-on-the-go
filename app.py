from wsgiref.util import request_uri
from flask import Flask, jsonify, request
import os
import random
import string
from pymongo import MongoClient
import requests
from datetime import datetime

app = Flask(__name__)
m = MongoClient("mongodb://poridhimongo:poridhi@36.255.70.114:27017/?authSource=admin", connect=False)
mongo = m["lab-ledger"]

@app.route("/alive", methods=["GET"])
def alive():
    resp = jsonify({"ping": "pong"})
    return resp, 200
@app.route("/launch-vm", methods=["GET"])
def launchVM():
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    port = random.randint(2000, 4000)
    os.system('echo "port={} name=sshserver-{} opn=ssh ./launchserver.sh" > /hostpipe'.format(port, name))
    resp = jsonify(
        {
            "status": "success",
            "command": f"ssh root@36.255.70.177 -p {port}", "password": "123456",
            "message": "Your lab on cloud will launch in a moment! Try after a few seconds"
        }
    )
    return resp, 200

@app.route("/launch-terminal", methods=["GET"])
def launchTerminal():
    token = request.headers.get('Authorization').split()[1]
    r=requests.get("http://36.255.68.85:5004/user/authenticate", headers={"Authorization": f"Bearer {token}"})
    print(r.status_code)
    if r.status_code != 200:
        resp = jsonify(
        {
            "status": "failed",
            "message": "Unauthorized"
        }
        )
        return resp, 401
    uid = r.json().get("uid")
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    port = random.randint(5000, 7000)
    os.system('echo "port={} name=termserver-{} ./launchserver.sh" > /hostpipe'.format(port, name))

    mongo.basic_lab.insert_one({"uid": uid, "creation_time": datetime.now()})
    resp = jsonify(
        {
            "status": "success",
            "url": f"http://36.255.70.177:{port}",
            "message": "Your lab on cloud will launch in a moment! Try after a few seconds"
        }
    )
    return resp, 200

def launch(port, name):
    os.system('echo "port={} name=sshserver-{} ./launchserver.sh" > /hostpipe'.format(port, name))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)