import json

from functions import override_file, conversations_json, static_conversations_json, prompts_todo_json

todo = []

with open(conversations_json, "r") as file:
    data = json.load(file)

override_file(static_conversations_json, data)

with open(static_conversations_json, "r") as file:
    data = json.load(file)
    for item in data:
        for key, value in item["mapping"].items():
            message = value["message"]
            if message is not None:
                if "author" in message and "role" in message["author"]:
                    role = message["author"]["role"]
                    if role == "user":
                        content = message["content"]
                        parts = content["parts"]
                        for part in parts:
                            todo.append({
                                "original": part,
                                "new": ""
                            })

override_file(prompts_todo_json, todo)
