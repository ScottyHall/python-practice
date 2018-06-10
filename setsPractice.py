# sets practice

# set.add has no effect if the element is already present
# sets do not contain duplicate elements

# define new set called example
example = set()

# add the data to the set after defining it
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

# print elements of set
print("The 'example' set = {0}".format(example))

print("The length of 'example' = {0}".format(len(example)))

# discard does nothing if element is not present
# remove throws an error if it is not present



# define a second set with pre-populated data rather than adding it later
example2 = set([28, True, 2.71828, "Helium"])
print("The length of 'example2' = {0}".format(len(example2)))

# clear the set quickly
example2.clear()

# union of sets = combination of all elements of sets
# intersection of sets = shared information of both sets

# evaluate the union of two sets
odds = set([1, 3 ,5, 7, 9])
evens = set([2, 4, 6 ,8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6,  8, 9, 10])

print("Union of sets, 'odds' and 'evens': {0}".format(odds.union(evens)))
print("Intersection of sets, 'odds' and 'primes': {0}".format(odds.intersection(primes)))

# check if number is inside a set
print("Is the number '2' a prime number?: {0}".format(2 in primes))
print("Is '6' an odd number?: {0}".format(6 in odds))
print("Is '9' an even number?: {0}".format(9 in evens))
