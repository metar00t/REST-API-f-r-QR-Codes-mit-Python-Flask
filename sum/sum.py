from flask import Flask

app = Flask(__name__)

@app.route("/sum/<int:first>/<int:second>")
def sum(first,second):
    return f'{first + second}'