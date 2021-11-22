from abc import ABC
from apps.app import Person


class Woman(Person, ABC):
    def __init__(self):
        super(Woman, self).__init__()
        self.age = 18

    def eat(self):
        print("eat some")

    def say(self):
        print("Woman say hello")

    def run(self, params=None):
        print(f"Man 接收到的参数是：{params}")
