from flask import Flask, request, jsonify
from utils import decode_id_token, collector_client

app = Flask(__name__)


@app.route("/")
def index():
  return "<p>用户认证首页</p>"


@app.route("/token")
def resolving_token():
  id_token = request.args.get("id_token")
  try:
    user_info = decode_id_token(id_token)
    token = collector_client.query_user_token(user_info)
    data = {"rs": 0, "token": token, "user_info": user_info}
  except Exception as e:
    data = {"rs": 1, "error": str(e)}
  return jsonify(data)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8081)
