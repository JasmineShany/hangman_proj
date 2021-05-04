def add(num1, num2):
    print("The result is:", num1 + num2)

def are_lists_equal(list1, list2):
    list1_input = list1.sort()
    list2_input = list2.sort()
    if list1 == list2:
        print("True")
    else:
        print("False")

def longest (my_list):
    res = max(my_list, key=len)
    print (res)







