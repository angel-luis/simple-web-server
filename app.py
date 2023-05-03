from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/<name>")
def homepage_with_name(name="Anonymous"):
    return render_template("index.html", name=" " + name)
