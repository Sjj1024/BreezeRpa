import time

csv_path = "person.csv"


file = open(csv_path)

while 1:
    title = file.readline()
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        print(line)
