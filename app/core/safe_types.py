def safe_float(x, default=0.5):
    try:
        if x is None:
            return default
        return max(0.0, min(1.0, float(x)))
    except:
        return default


def safe_str(x, default=None):
    if x is None:
        return default
    x = str(x).strip()
    return x if x else default