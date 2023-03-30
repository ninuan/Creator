import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def first():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
