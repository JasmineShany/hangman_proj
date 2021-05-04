import math
numbers = "12345Y"
print(numbers[-1])

#slice task 3.3.3
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[-1:-57:-2])


#task 3.4.2
my_name = input ("please enter text")
first_letter = my_name[0]
#print(first_letter)

cut_remaining_string = my_name[1:]
#print(cut_remaining_string)

replace_name = cut_remaining_string.replace(first_letter, 'e')
print(first_letter+replace_name)

