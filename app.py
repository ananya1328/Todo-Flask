from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"{self.slno} - {self.title}"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

@app.route("/update/<int:slno>", methods=["GET", "POST"])
def Update(slno):
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo.query.filter_by(slno=slno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(slno=slno).first()
    return render_template("update.html", todo=todo)

@app.route("/delete/<int:slno>")
def Delete(slno):
    todo = Todo.query.filter_by(slno=slno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)

