from .forms import TaskForm
from . import app , db
from .models import Task
from flask import render_template

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/create", methods=["POST", "GET"])
def create_task():
    task_form = TaskForm()
    if task_form.validate_on_submit():
        title = task_form.title.data
        description = task_form.description.data
        due_date = task_form.due_date.data
        print(title, description, due_date)
        new_task = Task(title=title, description=description, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        return "Task added to the database!"
    return render_template("create_task.html", form=task_form)