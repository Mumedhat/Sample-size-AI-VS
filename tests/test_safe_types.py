import pytest
from app.core.safe_types import safe_float, safe_str

def test_safe_float_happy_path():
    assert safe_float(0.5) == 0.5
    assert safe_float(0.0) == 0.0
    assert safe_float(1.0) == 1.0
    assert safe_float(0) == 0.0
    assert safe_float(1) == 1.0
    assert safe_float("0.75") == 0.75

def test_safe_float_out_of_bounds():
    assert safe_float(-0.5) == 0.0
    assert safe_float(-10) == 0.0
    assert safe_float(1.5) == 1.0
    assert safe_float(10) == 1.0

def test_safe_float_error_cases():
    assert safe_float(None) == 0.5
    assert safe_float("invalid") == 0.5
    assert safe_float([]) == 0.5
    assert safe_float({}) == 0.5

def test_safe_float_custom_default():
    assert safe_float(None, default=0.8) == 0.8
    assert safe_float("invalid", default=0.2) == 0.2

def test_safe_str_happy_path():
    assert safe_str("hello") == "hello"
    assert safe_str("  hello  ") == "hello"
    assert safe_str("world\n") == "world"

def test_safe_str_conversion():
    assert safe_str(123) == "123"
    assert safe_str(0) == "0"
    assert safe_str(1.5) == "1.5"

def test_safe_str_error_cases():
    assert safe_str(None) is None
    assert safe_str("") is None
    assert safe_str("   ") is None

def test_safe_str_custom_default():
    assert safe_str(None, default="unknown") == "unknown"
    assert safe_str("", default="unknown") == "unknown"
    assert safe_str("   ", default="unknown") == "unknown"
