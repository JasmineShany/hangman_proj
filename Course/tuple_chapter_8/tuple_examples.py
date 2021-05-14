#Tuple is immutable - cant change also מחרוזת()

my_first_tuple = ()
print(type (my_first_tuple))
print(my_first_tuple)

friendly_tuple = (2.5, 3, "bannana")
smart_tuple = 2.5, "bannana"
print(friendly_tuple, smart_tuple)

one_value_tuple = (20)
print(type(one_value_tuple))

#more commands use on tuple
lunch_info = ("12:30", 3, "pizza", 266)
print(len(lunch_info))
print(lunch_info[0])
print(lunch_info[1:2])
print(str(lunch_info[3]) + " calories" + " OMG!!!")

# tuple assignment
(food, type, calories ) = ("bread", "whole weat", 266)
print(food, type)

#tupel function
def picnic_shopping(list_of_prices):
    total = sum(list_of_prices)
    is_total_ok = total < 150
    return total, is_total_ok
prices_for_picnic = [17.90, 23.5, 150]
money, is_budget_possible = picnic_shopping(prices_for_picnic)
print(money, is_budget_possible)

#string formatting %
fruit = "graps"
drink = "wine"
print ("the basket contains %s and %s." % (fruit, drink))

bottles_num, drink = 3, "wine"
print("the basket conatains %d bottles of %s." %(bottles_num, drink))

basket_content = 3, "wine"
print("the basket conatains %d bottles of %s." %(basket_content))


