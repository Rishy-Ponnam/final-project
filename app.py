
from flask import Flask, flash, redirect, render_template, request, session
import datetime
import urllib3
from urllib.parse import urlencode
import json

app = Flask(__name__)

http = urllib3.PoolManager()

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    x = http.request('GET','localhost:5001/index')
    db_students = json.loads(x.data.decode('utf-8'))
    return render_template("index.html", db_students=db_students)
