from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<p>Welcome to my Flask application!</p>"

@app.route("/masturbate")
def masturbation():
    return "<p>Masturbating is fun!</p>"