# tuples practice
# ordered in a sequence to be useful
# similar to list, but faster
import sys	#using getsizeof
import timeit

# list, sequence surrounded by bracket
# tuple, sequence surrouned by paren

# list
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# tuple
perfec_squares = (1, 4, 9, 16, 25, 36)

print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfec_squares))

# iterate over both sequences
for p in prime_numbers:
	print("Prime: ", p)
for s in perfec_squares:
	print("Squares: ", s)

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# create 1,000,000,000 lists
list_test = timeit.timeit(stmt = "[1,2,3,4,5]",
	number = 10)
# create 1,000,000,000 tuples
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)",
	number = 10)
# results with executing 1,000,000,000x
"""List time:  78.85733622702537
Tuple time:  17.484754628996598"""

print("List time: ", list_test)
print("Tuple time: ", tuple_test)

# one way to break down a tuple
survey = (27, "Vietname", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python = ", knows_python)

# more compact way to break down a tuple with the same fields
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2 	# must cover all values to unpack

print("Age = ", age)
print("Country = ", country)
print("Knows Python = ", knows_python)