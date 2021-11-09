def get_ele(name):
  ele_dict = {
    "客梯": {
      "箱式客梯": [],
      "观光电梯": [],
      "自动电梯": ["自动扶梯", "自动人行道"],
      "其他客梯": ["病床电梯", "宅梯"]
    },
    "货梯": {
      "箱式货梯": [],
      "其他货梯": ["杂物电梯", "汽车电梯"]
    },
    "其他": {
      "消防电梯": []
    }
  }
  for b_key in ele_dict:
    m_dict = ele_dict.get(b_key)
    if name in m_dict.keys():
      return b_key, name
    for m_key in m_dict:
      s_list = m_dict.get(m_key)
      if name in s_list:
        return b_key, m_key
  return "", ""


if __name__ == '__main__':
  b_key, m_key = get_ele("箱式客梯")
  print(f"大类：{b_key}, 中类:{m_key}")
