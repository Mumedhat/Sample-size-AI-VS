def normalize_population(text):

    if text is None:
        return None

    t = text.lower()

    if "patients" in t and any(c.isdigit() for c in t):
        return text  # valid structured form

    if "patients" in t:
        return text  # acceptable fallback

    return None


def normalize_intervention(text):
    if text is None:
        return None

    return text.strip()