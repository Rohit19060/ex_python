with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines_list=[]
    for i in lines:
        temp = i.replace("\n", "").strip()
        lines_list.append(temp)
    r = open("links.json", "w", encoding="utf-8")
    print(str('''{
    "watchLater": ['''), file=r)
    new_len = len(lines_list)//11
    for x in range(new_len):
        print(f'{{"id":"{lines_list[11*x]}","link":"{lines_list[11*x+1]}","thumb":"{lines_list[11*x+2]}","length":"{lines_list[11*x+3]}","title":"{lines_list[11*x+6]}","creator":"{lines_list[11*x+9]}","creator_link":"{lines_list[11*x+7]}"}},',file=r,end="")
    
    print(str(']}'), file=r)
