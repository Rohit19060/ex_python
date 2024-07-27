import json
import os
import re

import isodate
from googleapiclient.discovery import build

api_key = ""

youtube = build("youtube", "v3", developerKey=api_key)

base_filename = "video_details"


def sanitize_title(title):
    # Remove all non-alphabetic characters except spaces
    sanitized_title = re.sub(r"[^a-zA-Z\s]", "", title)
    return sanitized_title


def get_current_json_file_index(base_filename):
    """Returns the index of the current JSON file based on existing files."""
    index = 5
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


def get_video_details(video_ids):
    """Fetches video details for a list of video IDs."""
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics", id=",".join(video_ids)
    )
    response = request.execute()
    return response


def write_failed_query_to_file(search_query):
    """Writes a failed query to a file."""
    with open("failed_queries.txt", "a") as file:
        file.write(search_query + "\n")


def search_youtube_by_title(search_query):
    """Fetches video details and appends them to a JSON file."""
    print(f"Searching YouTube for {search_query}")
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        maxResults=1,  # Number of results to return
    )
    try:
        response = request.execute()
    except Exception as e:
        print(f"API request failed: {e} for {search_query}")
        return

    video_ids = [item["id"]["videoId"] for item in response.get("items", [])]
    if not video_ids:
        print(f"No videos found for {search_query}")
        write_failed_query_to_file(search_query)
        return

    video_details_response = get_video_details(video_ids)
    for video in video_details_response.get("items", []):
        duration = video["contentDetails"]["duration"]
        duration = isodate.parse_duration(duration)
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = (
            f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        )
        title = video["snippet"].get("title", "N/A")

        video_details = {
            "search_query": search_query,
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

        file_info["line_count"] += 1


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
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in reversed(lines):
        sanitized_query = sanitize_title(line.strip())
        search_youtube_by_title(sanitized_query)
