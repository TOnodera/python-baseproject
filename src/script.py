from flask import Flask
from flask import globals
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)


@app.route("/")
def top():
    return "top"


@app.route("/hello")
def hello_world():
    return "hello world"


def main():
    app.debug = True
    app.run()


if __name__ == "__main__":
    main()
