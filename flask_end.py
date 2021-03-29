import os

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods = ['GET', 'POST'])
def hello_word():
    return "Hello World"


#Testing Block
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
