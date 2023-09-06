# Exercise 1
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
# citys = ' '.join(places).split()
# print(citys)
milad = [i for i in filter(str.strip,places)]
print(milad)


# Exercise 2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
newlist = sorted(author, key=lambda name: name.split(" ")[-1].lower())
print(newlist)

# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# # F = (9/5)*C + 32
til = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
new_til = list(map(lambda c:  (c[0], (9/5) * c[1]+ 32), til))
print(new_til)

# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

def hi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return hi(num - 1) + hi(num - 2)
print(hi(3))
