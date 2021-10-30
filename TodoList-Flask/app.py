from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from datetime import datetime as dt
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class TaskList(db.Model):
    __tablename__ = 'taskList'
    id = db.Column(db.Integer, primary_key=True)
    taskId = db.Column(db.String(45), nullable=False)
    taskName = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.String(45), nullable=False)
    time = db.Column(db.String(255), nullable=False)


@app.route('/', methods=['GET'])
def index():
    data = TaskList.query.all()
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    data = TaskList.query.all()
    item = data[::-1][0].id
    taskId = "task"+str(item + 1)
    taskName = request.form.get('todolist')
    entry = TaskList(taskId=taskId,taskName=taskName,completed="no",time=dt.now())
    db.session.add(entry)
    db.session.commit()
    return index()

@app.route('/check', methods=['POST'])
def check():
    # taskid = request.form.get()
    return "<h2>Task Completed </h2>"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
