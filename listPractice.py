# lists practice python

# 2 ways to create a list, with the list method, or with brackets
example = list()
example = []

# set values at time of definition
primes = [2, 3, 5, 7, 11, 13]

# alternatively, append items later
primes.append(17)
primes.append(19)

print("First '8' prime numbers: {0}".format(primes))

# in sets, order does not matter. In lists, ORDER MATTERS

# access by index
print("First value of the list = {0}".format(primes[0]))

# -1 wraps around to the last value of the list
print("Last value of the list = {0}".format(primes[-1]))

# next to last = -2, etc
print("Second to last value = {0}".format(primes[-2]))

# you can only wrap around once


# slicing
# includes the start value, EXCLUDES the stopping value
print("Sliced list 2:5: {0}".format(primes[2:5]))

#includes the start, excludes the last value
print("Beginning slice to index 6: {0}".format(primes[0:-1]))

# lists can hold multiple data types in python
example = [128, True, "Alpha, 1.732, [64, False]"]
print("Print example list with multiple data types: {0}".format(example))

# lists will hold the same data in separate indecies if appended unlike a set, which does not

# create 2 separate lists
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# concatenation
# order matters again with lists
print(numbers + letters)
print(letters + numbers)




