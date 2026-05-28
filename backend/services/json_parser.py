import json
import re


def safe_json_parse(text: str):
    if not text:
        return None

    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            return None

    return None