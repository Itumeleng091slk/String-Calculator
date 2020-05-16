import re

regex = re.compile(r'\d+') # add one or more digits

def has_negatives(string):
    empty_string = ''

    for x in range(len(string)):
        if string[x] == '-' and string[x+1].isdecimal():
            empty_string += '-' + string[x+1] + ','

    return empty_string

def add(string):
      delimiter = ',' # handles multiple delimiters 

    if string.startswith('//'):
        delimiter = string[2] 
        string = string[3:]

    string = string.replace('\n',',') 
    # string_num = string.spilt(delimiter)
    
    
    sum = []
    numbers = regex.findall(string) # this line is telling the program to find all the regular expressions
    negatives = has_negatives(string)
        
    try:
        string[:-1]
    except:
        raise "This is invalid!" # Handles invalid inputs
    if negatives:
        raise Exception("Negatives are not allowed: " + negatives) # This exception is telling the program that if there is any negative numbers within the program that an error/ exception will be thrown.

    if string == '':
        return 0
    else:
        for x in numbers:

            if int(x) > 20:
                pass
            else:
                num = int(x)
                sum += num

        return sum
    
#print(add("//;\n31;2"))
# print(add("1,1"))
