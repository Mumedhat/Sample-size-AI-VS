import pytest
from app.agents.statistician import extract_sample_size

def test_extract_sample_size_valid_patterns():
    # Test n= / N= patterns
    assert extract_sample_size("n=100") == 100
    assert extract_sample_size("n = 50") == 50
    assert extract_sample_size("N=200") == 200
    assert extract_sample_size("N = 150") == 150
    assert extract_sample_size("The total N  =   75 in this study.") == 75

    # Test patients pattern
    assert extract_sample_size("120 patients were enrolled.") == 120
    assert extract_sample_size("A total of 300patients") == 300

    # Test participants pattern
    assert extract_sample_size("There were 45 participants.") == 45
    assert extract_sample_size("We recruited 250participants.") == 250

    # Test sample size of pattern
    assert extract_sample_size("with a sample size of 500") == 500
    assert extract_sample_size("sample size of   80 ") == 80

def test_extract_sample_size_case_insensitivity():
    # The regex ignores case for the text match.
    # While N and n are specifically covered, 'patients' and 'participants' etc should be case insensitive
    assert extract_sample_size("120 PaTiEnTs") == 120
    assert extract_sample_size("45 PARTICIPANTS") == 45
    assert extract_sample_size("SAMPLE SIZE OF 500") == 500

def test_extract_sample_size_none_matches():
    # Empty string
    assert extract_sample_size("") is None

    # No numbers present
    assert extract_sample_size("We enrolled patients in the study.") is None

    # Numbers but not matching the pattern
    assert extract_sample_size("There are 5 groups.") is None
    assert extract_sample_size("n is not given") is None
    assert extract_sample_size("The size is 100") is None

def test_extract_sample_size_first_match_priority():
    # Since patterns are checked in order, the first pattern found wins
    # n=100 comes before 50 patients in the pattern list
    assert extract_sample_size("n=100 and 50 patients") == 100
    assert extract_sample_size("50 patients with n=100") == 100  # n= is checked first in the loop!
