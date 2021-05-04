i = 0
while i < 5:
    print(i)
    i += 1

# the int before represent that the user input is numbers not text
user_input = 0
while user_input not in [5, 6, 7]:
    user_input = int(input("how many years bears sleep?"))
    print("your answer is:", user_input)

#print out the numbers small than 10 and stops when it reaches a number that divide in 2
g = 0
while g < 10:
    g += 1
    if g % 2 == 0:
        break
    print(g)

#print out the numbers small than 10 but skips the ones that divide in 2
k = 0
while k < 10:
    k += 1
    if k % 2 == 0:
        continue
    print(k)





