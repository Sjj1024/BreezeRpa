class Car(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name)


class Baoma(Car):
    def __init__(self, name):
        super().__init__(name)
        self.age = 19
        self.name = name

    def say(self):
        print("say")



if __name__ == '__main__':
    baoma = Baoma("baoma")
    baoma.run()