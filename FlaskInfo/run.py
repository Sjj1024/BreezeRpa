from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "首页"


if __name__ == '__main__':
    app.run()
