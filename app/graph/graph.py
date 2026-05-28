from langgraph.graph import StateGraph, END

from app.state.state import GraphState

from app.agents.extractor_qwen import extractor_qwen_node
from app.agents.extractor_llama import extractor_llama_node
from app.agents.extractor_deepseek import extractor_deepseek_node

from app.agents.normalizer import normalizer_node

from app.agents.consensus import consensus_node
from app.agents.statistician import statistician_node
from app.agents.aggregator import aggregator_node


# =====================================================
# BUILD GRAPH
# =====================================================

builder = StateGraph(GraphState)


# =====================================================
# START NODE
# =====================================================

def start_node(state):
    return state


builder.add_node("start", start_node)


# =====================================================
# EXTRACTOR NODES
# =====================================================

builder.add_node("qwen", extractor_qwen_node)
builder.add_node("llama", extractor_llama_node)
builder.add_node("deepseek", extractor_deepseek_node)


# =====================================================
# NORMALIZER NODE (IMPORTANT FIX)
# =====================================================

builder.add_node("normalizer", normalizer_node)


# =====================================================
# POST-PROCESSING NODES
# =====================================================

builder.add_node("consensus", consensus_node)
builder.add_node("statistician", statistician_node)
builder.add_node("aggregator", aggregator_node)


# =====================================================
# ENTRY POINT
# =====================================================

builder.set_entry_point("start")


# =====================================================
# FAN-OUT (PARALLEL EXECUTION)
# =====================================================

builder.add_edge("start", "qwen")
builder.add_edge("start", "llama")
builder.add_edge("start", "deepseek")


# =====================================================
# FAN-IN (JOIN BARRIER)
# =====================================================

def join_node(state):
    """
    Synchronization barrier for parallel extractors.
    Ensures all outputs exist before continuing.
    """
    return state


builder.add_node("join", join_node)


builder.add_edge("qwen", "join")
builder.add_edge("llama", "join")
builder.add_edge("deepseek", "join")


# =====================================================
# PIPELINE AFTER JOIN
# =====================================================

builder.add_edge("join", "normalizer")
builder.add_edge("normalizer", "consensus")
builder.add_edge("consensus", "statistician")
builder.add_edge("statistician", "aggregator")
builder.add_edge("aggregator", END)


# =====================================================
# COMPILE GRAPH
# =====================================================

app = builder.compile()