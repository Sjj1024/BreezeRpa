import os
import time
import pymysql
import copy
import csv

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    database="local_database",
    charset="utf8"
)

cursor = conn.cursor()


def read_xml():
    csv_path = "/Users/metrodata/Downloads/zyc_xk_customer_info.csv"
    total = sum(1 for line in open(csv_path)) - 1
    print(total)
    num = 0
    step_index = read_num()
    file = []
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        for index, values in enumerate(reader):
            if index == 0:
                print(values)
                create_table(values)
                step_index = read_num()
            else:
                num += 1
                if num > index_num:
                    file.append(tuple(values))
                    if num % 1000 == 0:
                        b = copy.deepcopy(file)
                        step_index = f.tell()
                        insert_mysql(b, step_index)
                        file.clear()
                        print('\r' f"当前已存入,{num / total * 100}%", end='', flush=True)
        b = copy.deepcopy(file)
        insert_mysql(b, num)
        file.clear()
        print(f"当前已存入,{num / total * 100}%")


def create_table(content):
    print("创建表")
    col_str = "CREATE TABLE LIST("
    for col in content:
        col_str += f"{col} VARCHAR(100)  NOT NULL,"
    col_str += "PRIMARY KEY(id))"
    print(col_str)
    try:
        cursor.execute(col_str)
        write_num(0)
    except Exception as e:
        print(e)
        if "You have an error in your SQL syntax" in str(e):
            print("创建表出错")
            raise Exception("创建表出错")
        else:
            print("表已存在")


def write_num(content):
    desktop_path = "num_acc.txt"
    with open(desktop_path, "w") as f:
        f.write(str(content))


def read_num():
    desktop_path = "num_acc.txt"
    if os.path.exists(desktop_path):
        with open(desktop_path, 'r') as f:
            return int(f.read())
    else:
        return 0


def insert_mysql(b, num):
    datas_str = ""
    for i in b:
        datas_str += f"{i},"
    datas_str = datas_str[:-1]
    sql = f"insert into LIST VALUES {datas_str}"
    try:
        cursor.execute(sql)
        conn.commit()
        write_num(num)
    except Exception as e:
        print(e)
        write_num(num - 1000)
        raise Exception("")


if __name__ == '__main__':
    start_time = time.time()
    read_xml()
    conn.commit()
    print("写入完成")
    end_time = time.time()
    during_time = end_time - start_time
    print("程序运行时间： %.8s s" % during_time)
