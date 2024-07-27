import http.client
import json

img_urls = []

local_arr = [
    "en-IN",
    "en-US",
    "en-GB",
    "en-CA",
    "en-AU",
    "en-NZ",
    "fr-FR",
    "de-DE",
    "ja-JP",
]

image_titles = []
unique_urls = []

for local in local_arr:
    conn = http.client.HTTPSConnection("bing.biturl.top")
    payload = ""
    headers = {"Accept": "application/json"}
    conn.request(
        "GET",
        "/?resolution=1920&format=json&index=0&mkt=" + local,
        payload,
        headers,
    )
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        x = json.loads(data)
        if "url" in x:
            url = x["url"]
            print(url)
            current_img = url.split("https://www.bing.com/th?id=OHR.")[1]
            if current_img[:8] in image_titles:
                continue
            image_titles.append(current_img[:8])
            unique_urls.append(url)
    else:
        print("/?resolution=1920&format=json&index=0&mkt=" + local)
        print("Error: " + str(res.status) + " " + res.reason)

print(unique_urls)
