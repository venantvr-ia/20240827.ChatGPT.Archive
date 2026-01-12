import json

from functions import override_file, prompts_todo_json, prompts_done_json, llm, prompt

chain = prompt | llm

done = []

with open(prompts_todo_json, "r") as file:
    data = json.load(file)

for item in data:

    if item["new"] == "":

        ai_message = chain.invoke(
            {
                "text": item["original"],
            }
        )

        # response = input("Voulez-vous continuer ? (oui/non) : ").strip().lower()
        response = ""

        if response in ["oui", "o", "yes", "y", ""]:
            item["new"] = ai_message.content

        override_file(prompts_done_json, data)
