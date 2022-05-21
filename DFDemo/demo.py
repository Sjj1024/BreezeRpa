import pandas as pd


def check_data():
    print("筛选数据")
    df = pd.read_excel("./demo班级体侧.xlsx")
    total_data = get_total_data(df)
    new_data = pd.DataFrame(columns=df.columns.values)
    # 遍历结果total_data，如果元素存在df就添加，不存在就新增
    for i in total_data:
        name, year = i
        if ((df['姓名'] == name) & (df['年份'] == year)).any():
            row = df[df['姓名'].isin([name]) & df['年份'].isin([year])]
            new_data = new_data.append(row)
        else:
            new_data = new_data.append({'姓名': name, '年份': year}, ignore_index=True)
    print(new_data)
    new_data.to_excel("全量数据.xlsx")


def get_total_data(df):
    df2 = df.groupby("姓名", as_index=False).count()
    max_value = df2["年份"].max()
    name_all = df2[df2["年份"] >= max_value]["姓名"].values[0]
    all_year = df[df["姓名"] == name_all]["年份"].values
    # all_user = set(df["姓名"].values)
    all_user = []
    [all_user.append(i) for i in df["姓名"].tolist() if i not in all_user]
    total_data = [(a, b) for a in all_user for b in all_year]
    return total_data


if __name__ == '__main__':
    check_data()
