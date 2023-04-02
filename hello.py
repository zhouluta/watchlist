from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello(name):
    return f"<p>hello, {escape(name)}!</p>"

@app.route("/user/<name>")
def user_page(name):
    return f"User: {escape(name)}"

@app.route("/test")
def test_url_for():
    print(url_for("hello"))
    print(url_for('user_page', name="jay"))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return "Test Page"