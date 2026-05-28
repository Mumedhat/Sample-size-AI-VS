from app.agents.extractor_qwen import extractor_qwen_node
from app.agents.extractor_llama import extractor_llama_node
from app.agents.extractor_deepseek import extractor_deepseek_node

from app.agents.consensus import consensus_node


state = {
    "text": "This is a randomized controlled trial comparing implants versus bridges in 120 patients."
}


# RUN EXTRACTORS
qwen_result = extractor_qwen_node(state)
llama_result = extractor_llama_node(state)
deepseek_result = extractor_deepseek_node(state)


# MERGE INTO STATE
state.update(qwen_result)
state.update(llama_result)
state.update(deepseek_result)


# RUN CONSENSUS
final_state = consensus_node(state)


print("\n===== CONSENSUS OUTPUT =====\n")
print(final_state)