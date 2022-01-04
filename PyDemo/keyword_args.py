def test(*args):
  print(args)
  for i in args:
    print(i)


test(1, 2, 3)

print("------------------")


def test(**kwargs):
  print(kwargs)
  keys = kwargs.keys()
  value = kwargs.values()
  print(keys)
  print(value)


test(a=1, b=2, c=3, d=4)

# 输出值分别为
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict_keys(['a', 'b', 'c', 'd'])
# dict_values([1, 2, 3, 4])