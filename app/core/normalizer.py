import re


STUDY_TYPE_MAPPING = {
    "randomized controlled trial": "RCT",
    "rct": "RCT",
    "cohort study": "cohort",
    "cohort": "cohort",
    "case control": "case-control",
    "case-control": "case-control",
    "cross sectional": "cross-sectional",
    "cross-sectional": "cross-sectional",
    "unclear": "unclear"
}


def normalize_study_type(text):

    if text is None:
        return "unclear"

    t = text.lower().strip()

    return STUDY_TYPE_MAPPING.get(t, text)


def normalize_population(text):

    if text is None:
        return None

    t = text.lower().strip()

    # patients (n=120)
    match = re.search(r'n\s*=\s*(\d+)', t)

    if match:
        return f"{match.group(1)} patients"

    # 120 patients
    match = re.search(r'(\d+)\s+patients', t)

    if match:
        return f"{match.group(1)} patients"

    return text


def normalize_intervention(text):

    if text is None:
        return None

    t = text.lower().strip()

    t = t.replace(" versus ", " vs ")
    t = t.replace(" versus", " vs")
    t = t.replace("versus ", "vs ")

    return t.strip()