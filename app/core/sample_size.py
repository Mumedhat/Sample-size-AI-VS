import math


def cohens_d(mean1, mean2, pooled_sd):
    return abs(mean1 - mean2) / pooled_sd


def sample_size_two_group_ttest(effect_size, alpha=0.05, power=0.80):
    """
    Approximate sample size calculation
    for two independent groups.
    """

    # standard Z values
    z_alpha = 1.96
    z_beta = 0.84

    numerator = ((z_alpha + z_beta) ** 2) * 2
    denominator = effect_size ** 2

    n = numerator / denominator

    return math.ceil(n)


_CLINICAL_CONTEXT_MAPPING = {
    "RCT": 0.5,
    "cohort": 0.3,
    "case-control": 0.4,
    "observational": 0.2,
    "unclear": 0.3
}


def estimate_effect_size_from_clinical_context(study_type):
    return _CLINICAL_CONTEXT_MAPPING.get(study_type, 0.3)