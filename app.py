from flask import Flask, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4232Q8z\n\xecsd]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sql'
db.init_app(app)

from sqlalchemy.sql import func

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    content = db.Column(db.String)
    to = db.Column(db.String)
    status = db.Column(db.String)

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

        c_post = Post.query.filter_by(content=content).first()
        if Post.query.filter_by(author=author, to=to, content=content).first() in Post.query.all():
            flash("Lời nhắn của bạn đã bị trùng lặp", "danger")
            return redirect(url_for('cfs'))

        new_post = Post(author=author, to=to, content=content, status='wait')
        db.session.add(new_post)
        db.session.commit()

        flash("Lời nhắn của bạn đang chờ được duyệt", "good")
        return redirect(url_for('cfs'))



    posts = Post.query.all()

    return render_template("cfs.html", posts=posts)

@app.route('/create')
def create():

    return render_template("create.html")

@app.route('/daylatrangadminbaomatnhatthegioi')
def admin():

    return render_template("admin.html")

@app.route('/dowload_database')
def dl_database():

    return send_from_directory(directory='instance', path=f"database.sql", as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)