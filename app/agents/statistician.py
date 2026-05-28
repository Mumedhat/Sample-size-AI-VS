import re


def extract_sample_size(text):

    patterns = [
        r"n\s*=\s*(\d+)",
        r"N\s*=\s*(\d+)",
        r"(\d+)\s*patients",
        r"(\d+)\s*participants",
        r"sample size of\s*(\d+)"
    ]

    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return int(m.group(1))

    return None


def infer_test(text):

    t = text.lower()

    if "randomized" in t:
        if "vs" in t or "versus" in t:
            return "independent t-test"

    if "pre" in t and "post" in t:
        return "paired t-test"

    if "more than two" in t or "3 groups" in t:
        return "ANOVA"

    if "categorical" in t or "proportion" in t:
        return "chi-square test"

    return "t-test (default for RCT)"


def effect_size(text):

    t = text.lower()

    if "randomized" in t:
        return 0.3

    return 0.2


def statistician_node(state):

    text = state.get("text", "")

    return {
        **state,
        "sample_size": extract_sample_size(text) or 0,
        "statistical_test": infer_test(text),
        "effect_size": effect_size(text)
    }