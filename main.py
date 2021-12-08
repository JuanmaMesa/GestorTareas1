from flask import Flask,render_template, request, redirect, url_for
import db
from models import Tarea
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False)



if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)