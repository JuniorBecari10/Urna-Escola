# run with 'flask run -h 0.0.0.0'

from flask import Flask, redirect, render_template, send_file, request

app = Flask(__name__)

app_name = "Urna Eletrônica"

candidates = {
  "43": {
    "name": "Cand 1",
    "votes": 0,
  },
  "55": {
    "name": "Cand 2",
    "votes": 0,
  }
}

# Static

@app.route("/style.css")
def style():
  return send_file("static/style.css")

@app.route("/script.js")
def script():
  return send_file("static/script.js")

# Routes

@app.route("/")
def index():
  return render_template("/index.html", title=app_name)

@app.route("/fim", methods=["POST"])
def fim():
  number = request.form.get("number")
  
  try:
    cand = candidates[number]

    cand["votes"] += 1

    name = cand["name"]
    votes = cand["votes"]

    print(f"Votou no candidato {name}. Ele tem {votes} voto(s).")
  except KeyError:
    print(f"Candidato com o número {number} não existe. Voto anulado.")
  
  print("\nTabela de votos:")
  for key in candidates:
    cand = candidates[key]
    votes = cand["votes"]
    print(f"{key} | {votes}")
  
  print()

  return redirect("/")