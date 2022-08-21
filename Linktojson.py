with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines_list = []
    for i in lines:
        temp = i.replace("\n", "").strip()
        lines_list.insert(0, temp)
    sorted_line_list = sorted(set(lines_list))
    r = open("links.json", "w")
    print(str('''{
    "link": ['''), file=r)
    x = 1
    for j in sorted_line_list:
        print('{"id":"', file=r, end="")
        print(x, file=r, end='",')
        print('"link":"', file=r, end="")
        print(j, file=r, end="")
        print('"},', file=r)
        x = x+1
    print(str(']}'), file=r)
