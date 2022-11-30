import pandas as pd
import random


def read_excel():
    head_row = pd.read_csv("123.csv")
    target = 1000000
    while True:
        length = head_row.shape[0]
        print(f"\r进度:{(length / target) * 100}%", end="", flush=True)
        if length >= target:
            break
        random_index = random.randint(0, head_row.shape[0]-1)
        new_row = head_row.iloc[random_index]
        new_row["id"] = length + 1
        head_row = head_row.append(new_row)
    print(f"\r目标数据长度:{head_row.shape[0]}，正在存储中...")
    head_row.to_csv(f"target{target}.csv", index=False)
    print("存储成功")


if __name__ == '__main__':
    read_excel()
