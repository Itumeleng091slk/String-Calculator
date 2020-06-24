import re


def add(string):
    string = delimiters(string)
    if string:
        return add_numbers_into(string)
    else:
        return 0

def delimiters(string):
    string = multiple_delimiters(string)
    string = string.replace('\n', ',')
    return string

def multiple_delimiters(string):
    if string.startswith('//'):
        delimiter_rule, string = string.split('\n', 1)
        delimiter = delimiter_rule[2:]
        string = string.replace(delimiter, ',')
    return string

def add_numbers_into(string):
    numbers = map(int, string.split(','))
    validate_numbers(numbers)
    return sum(numbers)

def validate_negative_numbers(numbers):
    if any(number < 0 for number in numbers):
        raise ValueError

print(delimiters("//4\n142"))
