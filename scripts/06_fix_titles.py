import json

from functions import override_file, static_conversations_json

with open(static_conversations_json, "r") as file:
    data = json.load(file)
    for item in data:
        title = str(item["title"])
        item["title"] = title.rstrip(".")

override_file(static_conversations_json, data)
