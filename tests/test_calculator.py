from string_Calculator.calculator import add_function
import pytest


def test_add_empty_str():
    result = add_function("")
    assert result == 0


# Test if it will output one number if your input is the same number
def test_add_one_number():
    result = add_function("4")
    assert result == 4
    # assert add_function("60") == 60


# Tests two numbers
def test_add_two_numbers():
    result = add_function("1,2")
    assert result == 3
    result = add_function("2,2")
    assert result == 4


# Tests multiple numbers
def test_add_many_numbers():
    result = add_function("1,2,3,4,5")
    assert result == 15
    result = add_function("5,4,3,2,1")
    assert result == 15


# Test if it can handle new lines between numbers instead of commas
def test_new_lines():
    result = add_function("1\n2,3")
    assert result == 6
    result = add_function("1\n2\n3\n4")
    assert result == 10


def test_add_delimiter():
    result = add_function("//;\n1;2")
    assert result == 3


# Supports different delimeters
def test_handle_diff_delimiters():
    result = add_function("//[*][%]\n1*2%3")
    assert result == 6
    result = add_function("//;\n1;2")
    assert result == 3
    result = add_function("//4\n142")
    assert result == 3


# Test if there are negatives and throw an error
def handle_negative_numbers():
    with pytest.raises(ValueError):
        result = add_function("-4")
    with pytest.raises(ValueError):
        result = add_function("1,-2")
    with pytest.raises(ValueError):
        result = add_function("1,2,-3,4,5,-6,7")
    with pytest.raises(ValueError):
        result = add_function("-1\n2,3")


# Test if any number bigger than 20 will be ignored
def test_ignores_integers_greater_than_or_equal_to_1000():
    result = add_function("2,1001")
    assert result == 2
    result = add_function("2,1451,5")
    assert result == 7
    result = add_function("2\n1001,4521,6,12")
    assert result == 20


# Test if delimeters can be of any length
def test_supports_any_len_delimeter():
    result = add_function("//[***]\n1***2***3")
    assert result == 6
    result = add_function("//[abc][777][:(]\n1abc27773:(1")
    assert result == 7


# # Tests invalid delimeters
def test_invalid_delimiters():
    result = add_function("//[***][%]\n1***2%3")
    assert result == 6
    result = add_function("//[*][%^%^%^][==]\n1*2%^%^%^3==4")
    assert result == 10



