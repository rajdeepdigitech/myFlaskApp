from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<p>Welcome to my Flask application!</p>"

@app.route("/about")
def about():
    return "<p>This is my about page!</p>"