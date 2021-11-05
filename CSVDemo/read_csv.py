import copy
import csv
import os

import pymysql
import time

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    database="local_database",
    charset="utf8"
)
cursor = conn.cursor()

# csv_path = "/Users/metrodata/Desktop/PyProject/MateroDemo/CSVDemo/person.csv"
csv_path = "person.csv"
total = sum(1 for line in open(csv_path))
print(f"总的数据量是:{total}")


div = 2


def read_csv():
    line_num = read_index()
    file = open(csv_path)
    while True:
        # 可以遍历迭代器
        for value in file.readlines(1000):
            # value = value.replace("\n", "")
            if line_num == 0:
                print(line_num)
                line_num += 1
                print("创建表")
                # line_list = [i.replace('"', "") for i in value.replace("\n", "").split(",")]
                # create_table(line_list, line_num)
            else:
                line_num += 1
                file.append(value)
                if line_num % div == 0:
                    b = copy.deepcopy(file)
                    save_index(line_num)
                    # insert_mysql(b, line_num)
                    # file.clear()
                    print('\r', f"当前已存入：{format(float(line_num) / float(total) * 100, '.2f')}%", end='', flush=True)
        if line_num == total:
            b = copy.deepcopy(file)
            insert_mysql(b, line_num)
            file.clear()
        print('\r', f"当前已存入,{format(float(line_num) / float(total) * 100, '.2f')}%", end='', flush=True)


def create_table(content, index):
    print("创建表")
    col_str = "CREATE TABLE LIST("
    for col in content:
        col_str += f"{col} VARCHAR(100)  NOT NULL,"
    col_str += "PRIMARY KEY(id))"
    print(col_str)
    try:
        cursor.execute(col_str)
        save_index(index)
    except Exception as e:
        print(e)
        if "You have an error in your SQL syntax" in str(e):
            print("创建表出错")
            raise Exception("创建表出错")
        else:
            print("表已存在")


def save_index(line_num):
    desktop_path = "line_num.txt"
    with open(desktop_path, "w") as f:
        f.write(f"{str(line_num)}")


def read_index():
    desktop_path = "line_num.txt"
    if os.path.exists(desktop_path):
        with open(desktop_path, 'r') as f:
            reads = f.read()
            if reads:
                return int(reads)
            else:
                return 0
    else:
        return 0


def insert_mysql(b, index_num):
    datas_str = ""
    for i in b:
        datas_str += f"{i},"
    datas_str = datas_str[:-1]
    sql = f"insert into LIST VALUES {datas_str}"
    try:
        cursor.execute(sql)
        conn.commit()
        save_index(index_num)
    except Exception as e:
        print(e)
        # write_num(num - div)
        raise Exception("")


if __name__ == '__main__':
    read_csv()
