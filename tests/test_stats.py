from app.core.sample_size import (
    estimate_effect_size_from_clinical_context,
    sample_size_two_group_ttest
)

effect = estimate_effect_size_from_clinical_context("RCT")

n = sample_size_two_group_ttest(effect)

print("Effect Size:", effect)
print("Sample Size Per Group:", n)