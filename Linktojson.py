import json


# Function to extract video ID from YouTube link
def extract_video_id(link):
    # Split the link at 'v=' and take the second part
    return link.split("v=")[1]


# Load the JSON data from a file
with open("input.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print("Loaded data:", len(data))

# Extract the video IDs
video_ids = [extract_video_id(item["link"]) for item in data]

# Write the video IDs to a new file, each on a new line
with open("output.txt", "w", encoding="utf-8") as file:
    print("Total number of videos:", len(video_ids))
    for video_id in video_ids:
        file.write(video_id + "\n")
