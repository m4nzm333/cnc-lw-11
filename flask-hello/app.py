from flask import Flask, request, redirect, url_for, jsonify, render_template

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template("welcome.html")

app.run('0.0.0.0', 80, debug=True)