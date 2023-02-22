import random


def random_dic(dicts):
    dict_key_ls = list(dicts.keys())
    random.shuffle(dict_key_ls)
    new_dict = {}
    for key in dict_key_ls:
        new_dict[key] = dicts.get(key)
    return new_dict


if __name__ == '__main__':
    demo_dict = {
        'google': 'android',
        'facebook': 'whatsapp',
        'microsoft': 'windows',
        'apple': 'mac',
    }
    print(demo_dict)
    print(random_dic(demo_dict))