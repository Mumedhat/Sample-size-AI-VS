from services.json_parser import safe_json_parse

bad_output = 'Here is result: {"study_type": "RCT", "value": 1} end text'

print(safe_json_parse(bad_output))