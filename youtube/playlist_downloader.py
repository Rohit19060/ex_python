import json
import os
import re

import isodate
from googleapiclient.discovery import build

api_key = ""

youtube = build("youtube", "v3", developerKey=api_key)

# request = youtube.playlistItems().list(
#     part="snippet", playlistId="PL3-Wy9Q2edEboK_u0VnYcwtIJYXuzszYS", maxResults=55
# )
video_id = "XCrZleaIUO4"
request = youtube.videos().list(part="snippet,contentDetails,statistics", id=video_id)
response = request.execute()

base_filename = "video_details"

def extract_video_id(url):
    """Extracts video ID from a YouTube URL."""
    match = re.search(
        r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})",
        url,
    )
    return match.group(1) if match else None


def get_current_json_file_index(base_filename):
    """Returns the index of the current JSON file based on existing files."""
    index = 1
    while os.path.isfile(f"{base_filename}_{index}.json"):
        index += 1
    return index


def get_json_file_lines(filename):
    """Counts the number of lines in a JSON file."""
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return 0


def append_video_details_and_save(video_id):
    """Fetches video details and appends them to a JSON file."""
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics,liveStreamingDetails,recordingDetails,localizations",
        id=video_id,
    )
    try:
        response = request.execute()
    except Exception as e:
        print(f"API request failed: {e} for {video_id}")
        return

    # Append new data
    if response["items"]:
        video = response["items"][0]
        duration = video["contentDetails"]["duration"]
        duration = isodate.parse_duration(duration)
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = (
            f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        )
        title = video["snippet"].get("title", "N/A")
        print(f"Got video details for {video_id}: {title}")

        video_details = {
            "title": title,
            "duration": duration_str,
            "published_at": video["snippet"].get("publishedAt", "N/A"),
            "view_count": video["statistics"].get("viewCount", "N/A"),
            "like_count": video["statistics"].get("likeCount", "N/A"),
            "channelTitle": video["snippet"].get("channelTitle", "N/A"),
            "thumbnailUrl": video["snippet"]
            .get("thumbnails", {})
            .get("maxres", {})
            .get("url", "N/A"),
            "details": video,
        }
        # Check if we need to switch to a new file
        if file_info["line_count"] >= 1000:
            file_info["index"] += 1
            file_info["current_file"] = create_new_file(
                file_info["base_filename"], file_info["index"]
            )
            file_info["line_count"] = 0

        # Read existing data and append new details
        try:
            with open(file_info["current_file"], "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"items": []}

        data["items"].append(video_details)

        # Write updated data back to file
        with open(file_info["current_file"], "w") as file:
            json.dump(data, file, indent=4)

        file_info["line_count"] += len(data["items"])
    else:
        print(f"No videos found for {video_id}")


file_path = "input.txt"


def create_new_file(base_filename, index):
    """Creates a new JSON file with the given index."""
    return f"{base_filename}_{index}.json"


file_info = {
    "base_filename": base_filename,
    "index": get_current_json_file_index(base_filename),
    "current_file": create_new_file(
        base_filename, get_current_json_file_index(base_filename)
    ),
    "line_count": get_json_file_lines(
        create_new_file(base_filename, get_current_json_file_index(base_filename))
    ),
}
# Read the file and process each link
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in reversed(lines):
        url = line.strip()
        video_id = extract_video_id(url)
        if video_id:
            append_video_details_and_save(video_id)
        else:
            print(f"Invalid YouTube URL: {url}")
