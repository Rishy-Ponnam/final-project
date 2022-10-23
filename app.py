
from flask import Flask, flash, redirect, render_template, request, session
import datetime
import urllib3
from urllib.parse import urlencode
import json
import random
app = Flask(__name__)

http = urllib3.PoolManager()

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/quote", methods=["GET", "POST"])
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    symbol = request.form.get("symbol")
    result = lookup(symbol)
    if not result:
        return apology("Invalid Symbol", 400)
    return render_template("quoted.html", name = result["name"], price = usd(result["price"]), symbol = result["symbol"])
