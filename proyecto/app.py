from flask import Flask, render_template, request
from logic import mejor_transporte

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    info = None
    if request.method == "POST":
        distancia = float(request.form["distancia"])
        info = mejor_transporte(distancia)
    return render_template("index.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)