import sys
import re

regex = re.compile(r'\d+')

def add(string):
    sum = 0
    numbers = regex.findall(string)
    negatives = calc_has_negatives(string)
    delimiter = ","
    if string.startswith('//'):
        delimiter = string[2]
        string = string[3:]
    string = string.replace('\n',delimiter)
    string_num = string.split(delimiter)
    sum_of_number = []
    negative_nums = []

    for number in string_num:
        try:
            numbers = int(number)
            if int(number) < 0:
                negative_nums.append(numbers)
        except ValueError:
            numbers = 0
        sum_of_number.append(numbers)
        
    if negative_nums:
        message = ','.join([str(numbers) for numbers in negative_nums])
        raise Exception('Negatives not allowed'+ message)
    return sum    

       
def calc_has_negatives(string):
    empty_string = ''
    for x in range(len(string)):
        if string[x] == '-' and string[x+1].isdecimal():
            empty_string += '-' + string[x+1] + ','
    return empty_string

def multiple_delimiters(string):
    if string.startswith('//'):
        delimiter_rule, string_multi = string.split('\n', 1)
        delimiter = delimiter_rule[2:]
        string = string.replace(delimiter, ',')
    return string

def add_numbers_into(string):
    numbers = map(int, string.split(','))
    add(numbers)
    return sum(numbers)


print(add("-1,-2,3,4"))
