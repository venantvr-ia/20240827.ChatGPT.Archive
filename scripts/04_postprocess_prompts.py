import json

from functions import override_file, prompts_done_json

with open(prompts_done_json, "r") as file:
    data = json.load(file)

    for item in data:
        if len(item["original"]) < 5:
            if str(item["original"]).lower() == "next":
                item["new"] = "Passe au point suivant..."
            if len(item["original"]) == 1:
                item["new"] = item["original"] + "."
            if len(str(item["original"]).strip()) == 2:
                item["new"] = item["original"]

override_file(prompts_done_json, data)
