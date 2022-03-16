from abc import ABC
from apps.app import Person


class ManMAnMan(Person, ABC):
    def __init__(self):
        super(ManMAnMan, self).__init__()
        self.name = "ManMAnMan"
        self.age = 18

    def eat(self):
        print("eat some")

    def say(self):
        print("Man say 你好")

    def run(self, params=None):
        print(f"{self.name} 接收到的参数是：{params}")
