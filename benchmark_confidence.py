import timeit
import time

setup_code = """
import random
import string
import app.core.confidence as confidence
from app.core.confidence import is_vague_population

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

test_cases = [
    "patients",
    "dental needs",
    "random test case",
    "some other long text that does not match and will be checked until the end",
] * 100
"""

test_code = """
for t in test_cases:
    is_vague_population(t)
"""

if __name__ == "__main__":
    iterations = 10000
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=iterations)
    print(f"Baseline best time for {iterations} iterations: {min(times):.6f} seconds")
