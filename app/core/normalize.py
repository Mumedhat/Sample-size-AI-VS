def normalize_study_type(text: str) -> str:

    if not text:
        return "unclear"

    text = text.lower().strip()

    mapping = {
        "rct": "randomized controlled trial",
        "randomized controlled trial": "randomized controlled trial",
        "randomised controlled trial": "randomized controlled trial",
        "randomized clinical trial": "randomized controlled trial",
        "clinical trial": "clinical trial",
        "cohort study": "cohort study",
        "case control": "case-control study",
    }

    return mapping.get(text, text)