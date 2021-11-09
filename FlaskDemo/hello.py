import time
from flask import Flask, request, render_template
import threading


class FlaskApp(Flask):
  def __init__(self, *args, **kwargs):
    super(FlaskApp, self).__init__(*args, **kwargs)
    self._activate_background_job()

  def _activate_background_job(self):
    def run_job():
      while True:
        print('执行后台任务')
        time.sleep(2)

    # t1 = threading.Thread(target=run_job)
    # t1.start()


app = FlaskApp(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route('/test', methods=['POST', 'GET'])
def test():
  print("收到")
  if request.method == "GET":
    print("GET")
  else:
    print('POST')
    username = request.data
    print(username)
  return "收到"


if __name__ == '__main__':
  app.run(host="192.168.71.228", port=8990)
