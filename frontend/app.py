from flask import Flask, render_template,request,redirect,url_for , flash , make_response
import json
import requests

import sys

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True , port = 5001)

