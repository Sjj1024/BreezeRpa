from flask import Flask,request,session

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  # if request.method == "POST":
  return "登陆页面"


if __name__ == '__main__':
    app.run()