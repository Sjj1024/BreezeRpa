import time

from flask import Flask
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
        t1 = threading.Thread(target=run_job)
        t1.start()


app = FlaskApp(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
