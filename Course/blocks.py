my_name = input("please enter your name:")
if my_name == "Jasmine":
    print("This is the best name ever!!")
else:
    pass #TODO: print("pick a new name!")

#This is an example for bug message=1, message is not defined we need to initialise the variable. message = ""
pet_num = int(input("how many pets do you have?"))
if pet_num > 2:
  message = "You are an animal lover!"
print(message)
