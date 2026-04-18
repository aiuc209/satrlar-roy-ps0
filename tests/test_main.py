import pytest

def convert_lines(lines):
    return [line[0].upper() + line[1:].lower() for line in lines]

def test_convert_lines():
    lines = ["HELLO WORLD", "PYTHON IS FUN", "TESTING IS KEY"]
    expected = ["Hello world", "Python is fun", "Testing is key"]
    assert convert_lines(lines) == expected

def test_convert_lines_empty():
    lines = []
    expected = []
    assert convert_lines(lines) == expected

def test_convert_lines_single():
    lines = ["HELLO"]
    expected = ["Hello"]
    assert convert_lines(lines) == expected
