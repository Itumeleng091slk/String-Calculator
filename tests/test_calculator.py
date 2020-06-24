from string_Calculator.calculator import add
import pytest

def test_add_empty_str():
    assert add("") == 0

# Test if it will output one number if your input is the same number
def test_add_one_number():
    assert add("1") == 1

# Tests two numbers
def test_add_two_numbers():
    assert add("1,2") == 3

# Tests multiple numbers
def test_add_many_numbers():
    assert add("1,2,3,4") == 10 

# Test if it can handle new lines between numbers instead of commas
def test_new_lines():
    assert add("1\n2,3") == 6

# Supports different delimeters
def test_diff_delimiters():
    assert add("//;\n1;2") == 3

# Test if there are negatives and throw an error
def rejects_negative_numbers():
      assert raises(ValueError, add, '-1')
      assert raises(ValueError, add, '1,-2')

# Test if any number bigger than 20 will be ignored
def test_more_than_twenty():
    assert add("//;\n1;2,21") == 3

# Test if delimeters can be of any length
def test_delimeter_len():
    assert add("//[***]\n1***2***3") == 6


# Tests  multiple delimeters
def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3") == 6
