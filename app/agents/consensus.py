from collections import defaultdict
import math


def clamp(x):
    return max(0.0, min(1.0, x))


def safe_confidence(c):

    try:
        if c is None:
            return 0.5

        return clamp(float(c))

    except:
        return 0.5


def weighted_vote(items):

    scores = defaultdict(float)

    for value, confidence in items:

        if value is None:
            continue

        confidence = safe_confidence(confidence)

        scores[value] += confidence

    # nothing extracted
    if len(scores) == 0:
        return None, 0.0

    total = sum(scores.values())

    # 🔥 CRITICAL FIX
    if total <= 0:
        return None, 0.0

    best = max(scores.items(), key=lambda x: x[1])[0]
    best_score = scores[best]

    agreement = best_score / total

    # entropy penalty
    entropy = 0.0

    for _, w in scores.items():

        p = w / total

        entropy -= p * math.log(p + 1e-8)

    max_entropy = math.log(len(scores) + 1e-8)

    diversity = (
        entropy / max_entropy
        if max_entropy > 0
        else 0
    )

    confidence = agreement * (1 - 0.4 * diversity)

    return best, clamp(confidence)


def consensus_node(state):

    ex = [
        state.get("qwen_extraction", {}),
        state.get("llama_extraction", {}),
        state.get("deepseek_extraction", {})
    ]

    study, study_c = weighted_vote([
        (e.get("study_type"), e.get("confidence"))
        for e in ex
    ])

    pop, pop_c = weighted_vote([
        (e.get("population"), e.get("confidence"))
        for e in ex
    ])

    inter, inter_c = weighted_vote([
        (e.get("intervention"), e.get("confidence"))
        for e in ex
    ])

    final_conf = (
        study_c +
        pop_c +
        inter_c
    ) / 3

    return {
        **state,

        "study_type": study or "unclear",

        "population": pop,

        "intervention": inter,

        "consensus_confidence": clamp(final_conf)
    }