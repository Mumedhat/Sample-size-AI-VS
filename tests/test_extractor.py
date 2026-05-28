import os
import sys

# needed because you're using Option B (PYTHONPATH workaround)
sys.path.append("D:/Samplesize-AI")

from app.agents.extractor import extractor_node

# fake input state (this mimics LangGraph later)
test_state = {
    "text": "This is a randomized controlled trial in dentistry comparing implants vs bridges in 120 patients."
}

result = extractor_node(test_state)

print("\n===== EXTRACTOR OUTPUT =====\n")
print(result)