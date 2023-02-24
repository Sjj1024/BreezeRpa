# 将csv文件转为elementUI组件使用的table数据
import json
import pandas as pd


def run(csv_path):
    print("run")
    res_list = []
    df = pd.read_csv(csv_path)
    for row in df.iterrows():
        # 遍历所有列，组合为字典
        row_dict = {}
        columns = df.columns
        for col in columns:
            row_value = row[1].get(col) if not pd.isna(row[1].get(col)) else ''
            row_dian = str(row_value).find(".")
            row_value = str(row_value)[:row_dian + 7]
            row_dict[col] = row_value
        res_list.append(row_dict)
    # 做一个限长处理，限制暂时10行数据
    res_list_limit = res_list[:11]
    res_list_str = json.dumps(res_list_limit)
    print(res_list_str)


if __name__ == '__main__':
    csv_path = "demo_chi2_p.csv"
    run(csv_path)
    run("demo_chi2_stat.csv")