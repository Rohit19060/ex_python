import os

with open("input.txt", "r", encoding="utf-8") as f:
    d = f.readlines()
    x = []
    for i in d:
        y = i.replace("\n", "")
        y = "\"" + y + "\","
        x.append(y)
    print(x)
with open("output.txt", "w", encoding="utf-8") as r:
    for i in x:
        print(i.encode("utf-8").decode("utf-8"), file=r)
