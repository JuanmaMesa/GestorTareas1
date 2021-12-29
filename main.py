from flask import Flask,render_template, request, redirect, url_for
import db
from models import Tarea
app = Flask(__name__)
@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))




if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)