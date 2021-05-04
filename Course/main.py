from Course.list_chapter_6.list_function import longest, are_lists_equal


def add(num1, num2):
    print("The result is:", num1 + num2)

def main():
    add(3,1)
    list_long = ["111", "234", "2000", "goru", "birthday", "09"]
    longest(list_long)
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    are_lists_equal(list1, list2)
    are_lists_equal(list1, list3)

if __name__ == "__main__":
    main()
