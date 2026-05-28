def validate_study(state):

    issues = []

    study_type = state.get("study_type")
    statistical_test = state.get("statistical_test")
    sample_size = state.get("sample_size", 0)
    effect_size = state.get("effect_size", 0)

    # RULE 1
    if study_type == "RCT" and statistical_test not in ["t-test", "ANOVA"]:
        issues.append("Possible mismatch between RCT and statistical test")

    # RULE 2
    if sample_size < 30:
        issues.append("Sample size may be underpowered")

    # RULE 3
    if effect_size > 1.5:
        issues.append("Effect size unusually large")

    # RULE 4
    if effect_size < 0.1:
        issues.append("Effect size unusually small")

    if len(issues) == 0:
        validity_score = 0.9
        bias_risk = "low"

    elif len(issues) == 1:
        validity_score = 0.7
        bias_risk = "moderate"

    else:
        validity_score = 0.4
        bias_risk = "high"

    return {
        "validation_issues": issues,
        "validity_score": validity_score,
        "bias_risk": bias_risk
    }