string = '[6, 8, 4, 3, 7, 2, 9, 10, 11, 12, 13, 14, 15, 20, 16, 22, 17, 21]'
string = string.lstrip('[')
string = string.rstrip(']')
string = string.split(', ')
questions = [int(num) for num in string if num.isdigit()]
print(questions)
