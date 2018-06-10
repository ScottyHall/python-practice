# Map, filter, reduce

import math
import statistics
from functools import reduce

def area(r):
	"""Area of a circle with radius 'r'"""
	return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method
areas = []
for r in radii:
	a = area
	areas.append(a)

# Method 2: Use 'ma' function

print(list(map(area, radii)))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
		("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
		("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] +32)

tempsToF = (list(map(c_to_f, temps)))
print(tempsToF)

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

outliersPositiveData = list(filter(lambda x: x > avg, data))
outliersNegativeData = list(filter(lambda x: x < avg, data))

print(outliersPositiveData)
print(outliersNegativeData)

# remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Columbia", "",
			"Ecuador", "", "", "Venezuela"]

filteredCountries = list(filter(None, countries))
print(countries)
print(filteredCountries)

# reduce function
# multiply all numbers in a list

# first 10 prime numbers
dataNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# reduce function example
multiplier = lambda x, y: x*y
reducedNumbers = reduce(multiplier, dataNumbers)
print(reducedNumbers)

# for loop function example
product = 1
for x in dataNumbers:
	product = product * x
print(product)


