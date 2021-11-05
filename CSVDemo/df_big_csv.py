import os
import time

from sqlalchemy import create_engine, String
import pandas as pd

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/local_database?charset=utf8')
# 控制批量读取的行数
read_rows = 1000


def read_csv():
    # csv_path = "/Users/metrodata/Downloads/customer_info.csv"
    csv_path = "person.csv"
    # 已经读取的行数
    saved_rows = read_num()
    print(f"开始跳过{saved_rows}条数据")
    # 开始读取文件
    if not saved_rows:
        skip_list = 0
    else:
        rows_list = [i for i in range(1, saved_rows + 1)]
        skip_list = lambda x: x in rows_list
    df = pd.read_csv(csv_path, chunksize=read_rows, header=0, skiprows=skip_list)
    # df = pd.read_csv(csv_path, chunksize=read_rows, header=0)
    # total = df.shape[0] # 读取太慢
    total = sum(1 for line in open(csv_path)) - 1
    print(f"一共有{total}行数据")
    for chunk in df:
        # 将读取的数据写入Mysql,dtype：执行数据类型,如果是字典，就会按照对应列指定,否则可能会让pd猜错，而导致存储失败
        chunk.to_sql('customer_info', con=engine, if_exists='append', dtype=String(50))
        # 记录写入列多少行
        saved_rows += chunk.shape[0]
        write_num(saved_rows)
        print(f"\r当前已存入：{format(float(saved_rows) / float(total) * 100, '.2f')}%", end="")
        # time.sleep(4)


def write_num(content):
    desktop_path = "rows_num.txt"
    with open(desktop_path, "w") as f:
        f.write(str(content))


def read_num():
    desktop_path = "rows_num.txt"
    if os.path.exists(desktop_path):
        with open(desktop_path, 'r') as f:
            reads = f.read()
            if reads:
                return int(reads)
            else:
                return 0
    else:
        return 0


if __name__ == '__main__':
    start = time.time()
    read_csv()
    end = time.time()
    print(f"\n程序总用时：{end - start}秒")
