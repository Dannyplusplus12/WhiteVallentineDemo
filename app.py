from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sql'
db.init_app(app)

from sqlalchemy.sql import func

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    content = db.Column(db.String)
    to = db.Column(db.String)


with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():

    return render_template("dashboard.html")

@app.route('/choose')
def choose():

    return render_template("choose.html")


@app.route('/cfs', methods=['GET', 'POST'])
def cfs():
    if request.method == 'POST':
        author = request.form['from']
        to = request.form['to']
        content = request.form['content']

        new_post = Post(author=author, to=to, content=content)
        db.session.add(new_post)
        db.session.commit()


    posts = Post.query.all()

    return render_template("cfs.html", posts=posts)

@app.route('/create')
def create():

    return render_template("create.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)