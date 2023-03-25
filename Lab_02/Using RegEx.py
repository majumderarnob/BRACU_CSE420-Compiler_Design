import re

def validity_checker(text):
    if re.match('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}',text):
        return 'Email'
    elif re.match('^www.[a-z0-9._%+-]+\.[a-z]{2,}',text):
        return 'Web'
    else:
        return 'Invalid Email/Web address.'

with open("input_file.txt") as file:
    count = int(file.readline())
    for i in range (count):
        input_text = file.readline()
        result = validity_checker(input_text)
        print(result+',',i+1)