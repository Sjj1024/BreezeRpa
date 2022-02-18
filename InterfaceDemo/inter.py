import abc


class Car(abc.ABC):
  @abc.abstractmethod
  def run(self):
    pass


class Benz(Car):
  def run(self):
    print("benz run")


class BMW(Car):
  pass


def run(car):
  """
  运行入口函数
  """
  car.run()


if __name__ == "__main__":
  benz = Benz()
  bmw = BMW()

  run(benz)
  run(bmw)
