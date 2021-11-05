import os
import time
import pymysql
import copy

div = 2

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
    csv_path = "/Users/metrodata/Downloads/customer_info.csv"
    # csv_path = "person.csv"
    total = sum(1 for line in open(csv_path)) - 1
    print(total)
    num = 0
    file = []
    with open(csv_path, "r") as f:
        index_num = read_num()
        f.seek(index_num)
        # reader = csv.reader(f)
        for index, values in enumerate(f):
            if index_num == 0:
                print(values)
                index_num += len(str(values + '\n').encode())
                line_list = [i.replace('"', "") for i in values.replace("\n", "").split(",")]
                create_table(line_list, index_num)
            else:
                num += 1
                index_num += len(str(values + '\n').encode())
                line_list = [i.replace('"', "") for i in values.replace("\n", "").split(",")]
                file.append(tuple(line_list))
                if num % div == 0:
                    b = copy.deepcopy(file)
                    insert_mysql(b, index_num)
                    file.clear()
                    print('\r', f"当前已存入：{format(float(num) / float(total) * 100, '.2f')}%", end='', flush=True)
        if num == total:
            b = copy.deepcopy(file)
            insert_mysql(b, index_num)
            file.clear()
        print('\r', f"当前已存入,{format(float(num) / float(total) * 100, '.2f')}%", end='', flush=True)


def create_table(content, index):
    print("创建表")
    col_str = "CREATE TABLE LIST("
    for col in content:
        col_str += f"{col} VARCHAR(100)  NOT NULL,"
    col_str += "PRIMARY KEY(id))"
    print(col_str)
    try:
        cursor.execute(col_str)
        write_num(index)
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
        write_num(index_num)
    except Exception as e:
        print(e)
        # write_num(num - div)
        raise Exception("")


if __name__ == '__main__':
    start_time = time.time()
    read_xml()
    conn.commit()
    print("\n写入完成")
    end_time = time.time()
    during_time = end_time - start_time
    print("程序运行时间： %0.8s s" % during_time)
