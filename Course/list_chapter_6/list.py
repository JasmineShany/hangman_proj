movies = ["titlennnnnnnn", "edge", "titanic", "1", "effort"]
print(movies[0])

letters = "science"
list_of_letters = list(letters)
print(list_of_letters)

print(movies[1:3])
print(letters[1:3])
print(movies[-1])
print(letters[-1])
print(movies * 2)
print(len(movies))

# append to list
movies.append("10jokes")
movies += ["10jokes"]
print(movies)

# change an item in list
movies[1] = "jasmine"
print(movies)

# remove an item from list, removes the first item
movies.remove("10jokes")
print(movies)

print("earn" in movies)

#count / sort

number_of = movies.count("10jokes")
print(number_of)

sort_list = movies.sort()
print(movies)

#sorted
sorted(movies, key=len)
print(movies)
