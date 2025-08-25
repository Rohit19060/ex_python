with open("input.txt", "r", encoding="utf-8") as f:
    d = f.readlines()
    x = []
    for i in d:
        y = i.strip()
        # Append it as json data and add it to the list
        if y not in x:
            x.append(y)

with open("output.txt", "w", encoding="utf-8") as r:
    for i in sorted(x):
        print(i, file=r)
