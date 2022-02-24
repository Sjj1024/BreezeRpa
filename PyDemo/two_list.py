def buji():
  print("补集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  # 方法1
  # ret_list = list(set(a_list) ^ set(b_list))
  # 方法2
  ret_list = list(set(a_list).difference(set(b_list)))
  # ret_list = list(set(b_list).difference(set(a_list)))
  print(ret_list)
  print(tuple(ret_list))
  for index, value in enumerate(a_list):
    print(index, value)


def jiaoji():
  print("交集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  res_list = list(set(a_list).intersection(set(b_list)))
  print(res_list)


def bingji():
  print("并集")
  a_list = [1, 2, 3, 4, 5]
  b_list = [1, 4, 5]
  res_list = list(set(a_list).union(set(b_list)))
  print(res_list)


def meige_num():
  num_list = [1, 4, 6, 7, 8, 89, 2, 2, 4, 6, 7, 2, 3, 4, 23, 5, 6, 2, 2]
  # 查找重复数据
  num_set = set(num_list)
  for n in num_set:
    if num_list.count(n) > 1:
      print(f"重复数据有: {n}")
  buffer_list = []
  for index, value in enumerate(num_list):
    buffer_list.append(value)
    if (index + 1) % 5 == 0 or (index + 1) == len(num_list):
      print(index, buffer_list)
      buffer_list.clear()


def map_fillter():
  some_dict = {
    "name": "wang",
    "age": "19"
  }
  if "19" in some_dict:
    print("在里面")


if __name__ == '__main__':
  jiaoji()
  # bingji()
  # buji()
  # meige_num()
  # map_fillter()
