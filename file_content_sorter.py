with open("input.txt", "r", encoding="utf-8") as f:
    d = f.readlines()
    x = []
    for i in d:
        y = i.strip()
        # Append it as json data and add it to the list
        x.append(y)
    x = sorted(set(x))

with open("output.json", "w", encoding="utf-8") as r:
    for i in x:
        print(i, file=r)
        print(",", file=r)
