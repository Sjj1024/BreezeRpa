import pandas as pd

df = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])

print(df)

print(df + 1)

print(df.add(1))

# 除法
print(df.div(10))

# 减法
print(df - [1, 2])
print(df.sub([1, 2], axis='columns'))
print(df.sub(pd.Series([1, 1, 1], index=['circle', 'triangle', 'rectangle']), axis='index'))

# 不同形状的df相乘
other = pd.DataFrame({'angles': [0, 3, 4]}, index=['circle', 'triangle', 'rectangle'])
print(df * other)

print(df.mul(other, fill_value=0))