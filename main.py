with open("input.txt", "r", encoding="utf-8") as f:
    d = f.readlines()
    x = []
    for i in d:
        y = i.replace("\n", "").strip()
        x.insert(0, y)
    b = sorted(set(x))
with open("output.txt", "w", encoding="utf-8") as r:
    for i in b:
        print(str(i).encode("utf-8").decode("utf-8"), file=r)
