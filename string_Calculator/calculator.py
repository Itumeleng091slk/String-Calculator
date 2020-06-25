import sys
import re

regex = re.compile(r'\d+')

def add(string):
    string = delimiters(string)
    if string:
        return add_numbers_into(string)
    else:
        return 0

def delimiters(string):
    string = multiple_delimiters(string)
    string = string.replace('\n', ',')
    sum = []
    numbers = regex.findall(string) # this line is telling the program to find all the regular expressions
    negatives = validate_negative_numbers(string)
    return string

def multiple_delimiters(string):
    if string.startswith('//'):
        delimiter_rule, string = string.split('\n', 1)
        delimiter = delimiter_rule[2:]
        string = string.replace(delimiter, ',')
    return string

def add_numbers_into(string):
    numbers = map(int, string.split(','))
    validate_negative_numbers(numbers)
    return sum(numbers)

def validate_negative_numbers(numbers):
    while True:
        try:
            any(number < 0 for number in numbers)
            break
        except ValueError:
            print("negatives are not allowed")

print(delimiters("//4\n142"))
print(add("//4\n142"))
