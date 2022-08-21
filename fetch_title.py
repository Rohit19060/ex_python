import urllib.request

import favicon
from bs4 import BeautifulSoup


def find_tdi(domain):
    page = urllib.request.urlopen(domain)
    soup = BeautifulSoup(page, features="lxml")
    title = soup.title.string
    metaTag = soup.find_all('meta')
    desc = str([meta.attrs['content']
                for meta in metaTag if 'name' in meta.attrs and meta.attrs['name'] == 'description']).replace("[", "").replace("]", "").replace(".", "").replace("'", "").replace("\"", "")
    icon = favicon.get(domain)[0][0]
    return title, desc, icon


def reading(readFile):
    with open(readFile, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines_list = []
        for i in lines:
            temp = i.replace("\n", "")
            lines_list.insert(0, temp)
        sorted_line_list = sorted(set(lines_list))
        r = open("Links_formatted.html", "a")
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
            try:
                title, desc, icon = find_tdi(j)
            except:
                title = j
                desc = ""
                icon = ""
                tempX = icon
            print(f'<a href="{j}" target="_blank"><div>{x}. {title}'.encode(
                "utf-8").decode("utf-8"), file=r)
            print(f'<h3>{desc}</h3>'.encode("utf-8").decode("utf-8"), file=r)
            try:
                temp = tempX.rindex("/")
                alt = str(tempX[temp + 1:]).replace(".png",
                                                    "").replace(".jpg", "")
            except:
                alt = ""
            print(
                f'<img src="{icon}" alt="{alt}" width="5%"></div></a><br>', file=r)
            x = x+1
        print(str('''</body></html>'''), file=r)


reading("input.txt")
