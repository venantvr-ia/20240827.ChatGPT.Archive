import json
from datetime import datetime

from functions import static_conversations_json, sanitize_filename, get_unique_filename

with open(static_conversations_json, "r") as file:
    data = json.load(file)
    for item in data:
        title = str(item["title"])
        md = {"title": title.rstrip("."), "date": str(item["create_time"]), "chat": []}

        got = False

        for key, value in item["mapping"].items():
            message = value["message"]
            if message is not None:
                if "author" in message and "role" in message["author"]:
                    role = message["author"]["role"]
                    if role in ["user", "assistant"]:

                        if role == "assistant":
                            got = True

                        content = message["content"]
                        if "parts" in content:
                            parts = content["parts"]
                            chat = {"role": role, "parts": parts}
                            md["chat"].append(chat)

        if got:
            filename = sanitize_filename(md["title"])

            unique_filename = get_unique_filename("md", filename, ".md")

            open(unique_filename, "w").close()
            with open(unique_filename, "w") as document:
                document.write("# {0}\n".format(md["title"]))
                date_time = datetime.fromtimestamp(float(md["date"]))
                date_francaise = date_time.strftime("%d/%m/%Y %H:%M:%S")
                document.write("Date : {0}\n".format(date_francaise))
                for chat in md["chat"]:
                    document.write("\n\n## {0} :\n{1}".format(str(chat["role"]).title(), '\n'.join(chat["parts"])))
