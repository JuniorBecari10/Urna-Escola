from flask import Flask, render_template, send_file

app = Flask(__name__)

app_name = "Urna Eletrônica"

# Static

@app.route("/style.css")
def style():
  return send_file("static/style.css")

# Routes

@app.route("/")
def index():
  return render_template("/index.html", title=app_name)