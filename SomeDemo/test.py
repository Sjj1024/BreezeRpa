import time

starttime = time.time()
time.sleep(2.1) #延时2.1s
endtime = time.time()
dtime = endtime - starttime

print("程序运行时间：%.8s s" % dtime)  #显示到微秒