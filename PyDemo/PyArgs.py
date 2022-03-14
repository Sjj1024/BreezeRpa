def say(*args):
  print(*args)


def play(**kwargs):
  print(kwargs)


if __name__ == '__main__':
  say(4, 5, 6, 6)
  play(name="song", age=9)
