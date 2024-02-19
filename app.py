from flask import Flask, render_template, jsonify

app = Flask(__name__)

async def get_data():
    for i in range(100000000):
        pass
    return "we do have something"


@app.route('/')
def hello_world():

    return render_template("dashboard.html")

@app.route('/choose')
def choose():

    return render_template("choose.html")


@app.route('/cfs')
def cfs():

    return render_template("cfs.html")

@app.route('/create')
def create():

    return render_template("create.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)