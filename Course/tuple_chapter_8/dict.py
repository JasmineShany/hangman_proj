#dict is mutable (changaeble) the keys are unique only one value to the key
my_first_dict = {}
print( type(my_first_dict))

keyboard_shortcuts = {"copy": "ctrl + c", "paste": "ctrl + v", "undo": "ctrl + z"}
print(keyboard_shortcuts)
print(keyboard_shortcuts["copy"])

keyboard_shortcuts ["cut"] = "ctrl + x"
print(keyboard_shortcuts)
keyboard_shortcuts ["paste"] = "shift + insert"
print(keyboard_shortcuts)


keyboard_info = {"Company": "Logitech", "Number of keys": 101, "Are emoji included?": True, "Language": "Hebrew"}
print(keyboard_info)

#delete from dict
del keyboard_shortcuts ["copy"]
print(keyboard_shortcuts)

keyboard_shortcuts.pop("paste")
print(keyboard_shortcuts)

print(keyboard_shortcuts.keys())
print(keyboard_shortcuts.values())

#for + dict
for key in keyboard_shortcuts.keys():
    print(key)

for value in keyboard_shortcuts.values():

    print(keyboard_shortcuts.values())

print(keyboard_shortcuts.items())
print(keyboard_shortcuts)
print(keyboard_shortcuts [1,2])

#TODO: finish the tasks in this chapter

