import pandas as pd
import random


def read_excel():
    head_row = pd.read_excel("123.xlsx")
    head = head_row.columns
    values = head_row.values
    head_row.sort_index()
    new_list = [*values]
    target = 1048575
    while True:
        print(f"\r进度:{(len(new_list) / target)*100}%", end="", flush=True)
        if(len(new_list) >= target):
            break
        new_row = new_list[random.randint(1, len(new_list)-1)]
        new_row[0] = len(new_list) + 1
        new_list.append(new_row)
    print(f"\r目标数据长度:{len(new_list)}，正在存储中...")
    target_pd = pd.DataFrame(new_list, columns=head)
    target_pd.to_excel(f"target{len(new_list)}.xlsx", index=False, engine='openpyxl')


if __name__ == '__main__':
    read_excel()
