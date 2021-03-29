import os

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_word():
    return render_template("sample.html")


@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello_word2(name):
    return "Hello, {}".format(name)


# Testing Block
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

