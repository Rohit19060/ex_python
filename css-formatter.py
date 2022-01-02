target = "input.css"

with open(target, "r", encoding="utf-8") as f:
    d = f.readlines()
    temp = []
    temp2 = []
    for i in d:
        if(len(i) >= 1):
            x = i.replace("\n", "").strip().casefold()
            if len(x) != 0 and x[-1:] != "{" and x[-1:] != "}" and x[-1:] != "," and x[-1:] != ";":
                x = x + ";"
            temp.append(x)
            if x[-1:] == "}":
                temp2.append(sorted(temp))
                temp = []

with open("output.css", "w", encoding="utf-8") as r:
    for a in sorted(temp2, reverse=True):
        for i in a:
            print(str(i).encode("utf-8").decode("utf-8"), file=r)
