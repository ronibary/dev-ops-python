from flask import Flask, render_template, request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from redis import Redis

app = Flask(__name__)

# Manually push the application context
app.app_context().push()

#redis = Redis(host='localhost', port=6379)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create instance of the db
db = SQLAlchemy(app)

# create the Table Todo , model
class Todo(db.Model): # pylint: disable=too-few-public-methods
    """A dummy docstring."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def pub1(self):
        """A dummy docstring."""
        print("")

    def pub2(self):
        """A dummy docstring."""
        print("")


@app.route("/edit")
def home1():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/")
def list1():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    """A dummy docstring."""
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home1"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home1"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home1"))

# @app.route('/')
# def hello():
#     redis.incr('hits')
#     return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')



# @app.route('/')
# def home():
#     return 'Hi Everyone'
#
#
# @app.route('/base')
# def home1():
#     return render_template("base.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
