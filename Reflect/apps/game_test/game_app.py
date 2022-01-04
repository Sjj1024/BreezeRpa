from apps.app import Person


class GameTest(Person):
    def __init__(self):
        super(GameTest, self).__init__()
        self.age = 18

    def eat(self):
        print("eat some")

    def say(self):
        print("GameTest say hello")

    def run(self, params=None):
        print(f"GameTest 接收到的参数是：{params}")
