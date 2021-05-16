import os

my_first_file = open(os.path.expanduser(r"~/Desktop/Jasmine/jasmine_pythin_example.txt"))
for line in my_first_file:
    if "Death" not in line:
        print(line)
my_first_file.close()

#the "w" modify the text and run over the old text
my_first_file = open(os.path.expanduser(r"~/Desktop/Jasmine/jasmine_pythin_example.txt"), "w")
my_first_file.write("I am amazing!!!!!!!!!!!!!!!!!!!!!")
my_first_file.close()
print(my_first_file)



