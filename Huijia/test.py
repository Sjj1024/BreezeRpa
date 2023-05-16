i = int(input("请输入一个数值"))
# qw=int
# sw=int
# bw=int
# gw=int
n = int
if i <= 9999:
    n = i * i
    qw = n // 1000
    bw = n // 100 % 10
    sw = n // 10 % 10
    gw = n % 10
    print(f"条件结果是: {qw == bw and sw == gw and qw != sw}")
    if qw == bw and sw == gw and qw != sw:
        print("豫A" + str(qw) * 2 + str(sw) * 2)
    else:
        i = i + 1
        print(f"i的值是:{i}")
else:
    print("错误")
