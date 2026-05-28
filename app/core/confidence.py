import re


def has_numeric_population(text):

    if text is None:
        return False

    return bool(re.search(r'\d+', text))


def is_vague_population(text):

    if text is None:
        return True

    vague_terms = [
        "patients",
        "subjects",
        "participants",
        "people",
        "individuals",
        "patients with",
        "dental needs"
    ]

    t = text.lower().strip()

    return t in vague_terms or len(t.split()) <= 2


def valid_intervention(text):

    if text is None:
        return False

    t = text.lower()

    keywords = [
        "vs",
        "versus",
        "compared",
        "comparison",
        "implant",
        "bridge",
        "treatment"
    ]

    return any(k in t for k in keywords)


def compute_extraction_confidence(data):

    score = 0.0

    study_type = data.get("study_type")
    population = data.get("population")
    intervention = data.get("intervention")

    # study type
    if study_type and study_type != "unclear":
        score += 0.4

    # population
    if population:

        if has_numeric_population(population):
            score += 0.35

        elif not is_vague_population(population):
            score += 0.15

    # intervention
    if intervention and valid_intervention(intervention):
        score += 0.25

    return round(min(score, 1.0), 2)