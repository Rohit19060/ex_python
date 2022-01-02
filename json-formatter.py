def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines_list = []
    for i in lines:
        temp = i.replace("\n\n\n", "")
        lines_list.insert(0, temp)
    lines = Reverse(lines_list)
    properties = []
    descriptions = []
    count = 0
    for i in lines:
        if (count % 2 == 0):
            properties.insert(0, i.replace("\n", ""))
        else:
            descriptions.insert(0, i.replace("\n", ""))
        count += 1

properties = Reverse(properties)
descriptions = Reverse(descriptions)

with open("output.json", "w", encoding="utf-8") as r:
    print(str('['), file=r)
    for a in range(0, len(properties)):
        print("{ \"property\": \"" +
              properties[a] + "\",\n \"Description\": \"" + descriptions[a] + "\"},", file=r)
    print(str(']'), file=r)
