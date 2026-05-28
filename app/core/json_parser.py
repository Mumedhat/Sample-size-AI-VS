import json
import re


def extract_json(text):

    try:
        # direct parse
        return json.loads(text)

    except:

        # find JSON block
        match = re.search(r'\{.*\}', text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except:
                pass

    return None