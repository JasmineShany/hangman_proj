def this_is_my_first_function():
    print("You are cool!")


this_is_my_first_function()


def square(number):
    print(number ** 3)

square(4)

#Global and Local param
fish_num = 6
def fish_food():
    food_for_fish = 9
    print (fish_num * food_for_fish)
fish_food()

#Change Local and Global
animal = "Rabbit"
def water():
    global animal
    animal = "goldfish"
    print(animal)

water()
print(animal)


def num_of_oranges (small_cups, big_cups = 9):
    oranges_results = small_cups + big_cups * 3
    return oranges_results

oranges_needed = num_of_oranges(6)
kg_needed = oranges_needed / 5
print ("Today yo will need", oranges_needed, "oranges")
print ("You will need to buy", kg_needed, "kg oranges")

# help(num_of_oranges(3,9))
# num_of_oranges(6, 8).__doc__