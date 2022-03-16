import abc


class Person(object):
    my_type = "person type"

    def __init__(self):
        self.name = "wan"
        self.route = "路由"

    @abc.abstractmethod
    def say(self):
        print(self.name)

    @abc.abstractmethod
    def run(self, params=None):
        pass
