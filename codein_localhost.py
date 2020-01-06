import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("codein_temp.html")







if (__name__ == "__main__"):
    app.run(host="127.0.0.1",port=8080)
