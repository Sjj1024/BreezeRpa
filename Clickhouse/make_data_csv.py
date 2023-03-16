import pandas as pd
import numpy as np
import random

intersection_num = 1000  # 交集的大小
same = random.sample(range(10 ** 7, 10 ** 8), intersection_num)
fs = open('50w.csv', 'w')
for i in same:
    print("%018d" % i, file=fs)
fs.close()

snum = []
for i in range(1, 11):
    a = ''.join(['x', str(i)])
    snum.append(a)
print(snum)

# data=pd.read_csv('20w.csv',names=['id'])
data1 = pd.read_csv('50w.csv', names=['id'])
data1[snum] = pd.DataFrame(np.random.randint(-100, 1000000, size=(1000, 10)))
data1['y'] = pd.DataFrame(np.random.randint(0, 2, size=(1000, 1)))
data1.to_csv('guest500wei_50w.csv', index=0)

data2 = pd.read_csv('50w.csv', names=['id'])
# size 多少行多少列
data2[snum] = pd.DataFrame(np.random.randint(-100, 1000000, size=(1000, 10)))
# data2['y']=pd.DataFrame(np.random.randint(0,2,size=(1000,1)))
data2.to_csv('host500wei_50w.csv', index=0)