import os


def say(*args):
  print(*args)


def play(**kwargs):
  print(kwargs)


def get_enviroment():
  print(os.environ)
  # os.environ["TEST_NAME"] = "123456"
  # print(os.environ)


def try_else():
  try:
    a = "a"
    b = int(a)
  except Exception as e:
    print(e.with_traceback(None))
  else:
    print("no error")


if __name__ == '__main__':
  # say(4, 5, 6, 6)
  # play(name="song", age=9)
  # get_enviroment()
  try_else()