with open("mark1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines_list = []
    for i in lines:
        temp = i.replace("\n", "").strip()
        lines_list.insert(0, temp)
    sorted_line_list = sorted(set(lines_list))
with open("mark1.txt", "w", encoding="utf-8") as r:
    for a in sorted_line_list:
        print(str(a).encode("utf-8").decode("utf-8"), file=r)
    r = open("Links_formatted.html", "w", encoding="utf-8")
    print(str('''<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Read Laters</title>
                </head>
                <style>
                body {
                    margin: 10px 10%;
                }
                a {
                    text-decoration: none;
                    display: block;
                    margin: 2%;
                    font-size: 20px;
                    padding: 20px;
                    background-color: black;
                    color: white;
                    border-radius: 20px;
                    word-wrap: break-word;
                    text-transform: capitalize;
                }
                a:hover {
                    background-color: rgb(218, 218, 218);
                    color: black;
                }
                </style>
                <body>'''), file=r)
    x = 1
    for j in sorted_line_list:
        print(
            f'<a href="{j}" target="_blank"><p>{x}. {j}</p></a>'.encode("utf-8").decode("utf-8"), file=r)
        x = x+1
    print(str('''</body></html>'''), file=r)
