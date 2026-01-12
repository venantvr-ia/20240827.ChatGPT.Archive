import re

from bs4 import BeautifulSoup

from functions import override_file, chat_html

with open(chat_html, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    script_tag = soup.find("script", text=re.compile(r'var\s+jsonData\s*='))

if script_tag:
    js_code = script_tag.string
    # noinspection PyUnresolvedReferences
    script_tag.string.replace_with("var jsonData = null;")
    override_file(chat_html, str(soup))
