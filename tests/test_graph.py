import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.graph.graph import app


input_state = {
    "text": "This is a randomized controlled trial comparing implants versus bridges in 120 patients."
}

result = app.invoke(input_state)

print("\n===== FINAL OUTPUT =====\n")
print(result)