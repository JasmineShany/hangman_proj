# Show variables usage
egg_number = 4
ducklings_num = egg_number
brothers_num = ducklings_num - 1
print(brothers_num)

# Show change of variables
a = 10
b = a
a = 4
print(a, b)

# Bool variable
I_am_hungry = True
number_of_sandwich = 7
cups_of_coffee = 6
I_am_hungry = (number_of_sandwich == 3) and (cups_of_coffee == 6)
print(I_am_hungry)

# in state
print("I" in "I am")
print("b" in "food")

# input
name = input("please enter your name")
print("Hello", name)

#Casting variables (הסבה)
number = input("whats your number?")
print(int(number) + 2)

#Change places of variables
Jill_lives = "Herzelia"
Jhon_lives = "Tel-Aviv"
Jhon_lives, Jill_lives = Jill_lives,Jhon_lives
print (Jhon_lives,Jill_lives)



