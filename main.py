from flask import Flask
app = Flask(__name__)


def hello():
    return 'Hello!'
app.add_url_rule('/hi', 'hello', hello)

if __name__ == '__main__':
    app.run(debug = True)