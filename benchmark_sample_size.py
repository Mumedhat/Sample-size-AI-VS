import timeit

setup_code = """
from app.core.sample_size import estimate_effect_size_from_clinical_context
"""

test_code = """
estimate_effect_size_from_clinical_context("RCT")
estimate_effect_size_from_clinical_context("cohort")
estimate_effect_size_from_clinical_context("unknown")
"""

times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=100000)
print(f"Baseline Time: {min(times)}")
