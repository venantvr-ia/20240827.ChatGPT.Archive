import json

from functions import override_file, prompts_done_json, static_conversations_json

with open(prompts_done_json, "r", encoding="utf-8") as json_file:
    tokens = json.load(json_file)

with open(static_conversations_json, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

    for item in data:
        for key, value in item["mapping"].items():
            message = value["message"]
            if message is not None:
                if "author" in message and "role" in message["author"]:
                    role = message["author"]["role"]
                    if role == "user":
                        content = message["content"]
                        parts = content["parts"]
                        for i in range(len(parts)):
                            part = parts[i]
                            for token in tokens:
                                if str(token["original"]).strip() == str(part).strip():
                                    parts[i] = token["new"]

override_file(static_conversations_json, data)
