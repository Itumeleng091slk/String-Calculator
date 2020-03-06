from string_Calculator.calculator import add
import pytest
# check = has_nagtives()
# checks = add()
# Test if string is empty
def test_add_empty_str():
    assert add("") == 0

# Test if it will output one number if your input is the same number
def test_add_one_number():
    assert add("1") == 1

# Test if it can add two numbers
def test_add_two_numbers():
    assert add("1,2") == 3

# Test if it can add multiple numbers
def test_add_many_numbers():
    assert add("1,2,3,4") == 10 

# Test if it can handle new lines between numbers instead of commas
def test_new_lines():
    assert add("1\n2,3") == 6

# Test if it support different delimeters
def test_diff_delimiters():
    assert add("//;\n1;2") == 3

# Test if there are negatives and throw an error
def test_check_negatives():
    with pytest.raises(Exception) as err:
        assert add("//;\n-1;2,-3")
        assert str(err.value) == "Negatives not allowed: -1,-3,"    

# Test if any number bigger than 20 will be ignored
def test_more_than_twenty():
    assert add("//;\n1;2,21") == 3

# Test if delimeters can be of any length
def test_delimeter_len():
    assert add("//[***]\n1***2***3") == 6


# Tests if it can allow multiple delimeters
def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3") == 6
