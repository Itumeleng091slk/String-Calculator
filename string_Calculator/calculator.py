import re

def sum_function(num_list):
	sum =0 
	for numbers in num_list:
		if numbers == '':
			num = 0
		else:
			num = int(numbers)
			if num < 0:
				raise ValueError('Negatives are not allowed')
			elif num >= 1000:
				num = 0
		sum += num
	return sum

def has_negatives(string):
    empty_string = ''
    for numbers in range(len(string)):
        if string[number] == '-' and string[number+1]:
            empty_string += '-' + string[number+1] + ','
    return empty_string

def add_function(number:str) -> int:
	find_regex = re.search('^//(.*)', number)
	if number == '':
		num_list = []
	elif '[' in number:
		count_space = 0
		for numbers in number:
			if numbers == '[':
				count_space += 1
		delims = r'\[(.*)]' * count_space
		search_regex = re.search(f'^//{delims}+', number)
		if search_regex:
			delim = ''
			for numbers in range(count_space):
				delim += search_regex.groups()[numbers]
			num_list =  re.split(r'['+delim+r'\n\]//[]', number[(4) + len(delim):])
	elif find_regex:
		delim = find_regex.groups()[0]
		num_list = re.split(r'['+delim+'\n]', number[(3) + len(delim):])
	else:
		num_list = re.split('[,\n]', number)
	return sum_function(num_list)
