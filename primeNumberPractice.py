# Prime number practice
import time
import math

# The first program v1 is slow, check below for v2 improvements
"""
18	= 1*18
	= 2*9
	= 3*6
	= sqrt(18) * sqrt(18) after the square root of the variable, the factors are the same, but reversed.

	This is how version2 can be sped up."""

def is_prime_v1(n):
	"""Return 'True' if 'n' is a prime number."""
	if n == 1:
		return False	# 1 is not prime

	for d in range(2, n):
		if n % d == 0:
			return False
	return True

""" testing function output for prime numbers 1 - 20
for n in range(1, 21):
	print(n, is_prime_v1(n))"""

# time function test for prime_v1
"""
t0 = time.time()
for n in range(1, 100000):
	is_prime_v1(n)
	if n % 10000 == 0:		# print message every 10000 numbers so they know it's running
		print("{0}% Calculated".format(n/1000))
t1 = time.time()
print("\n\n100% Calculated")
print("Time required v1: ", t1 - t0)"""

# better, but v2 still has room for improvment
def is_prime_v2(n):
	"""Return 'True' if 'n' is a prime number."""
	if n == 1:
		return False

	max_divisor = math.floor(math.sqrt(n))
	for d in range(2, 1 + max_divisor):
		if n % d == 0:
			return False
	return True

"""
# testing function for prime_v2 1-20
for n in range(1, 21):
	print(n, is_prime_v2(n))"""

# time function test for prime_v2
t0 = time.time()
for n in range(1, 1000000):
	is_prime_v2(n)
	if n % 10000 == 0:		# print message every 10000 numbers so they know it's running
		print("{0}% Calculated".format(n/10000))
t1 = time.time()
print("Time required v2: ", t1 - t0)

# v3 takes out the step of checking 
def is_prime_v3(n):
	"""Return 'True' if 'n' is a prime number."""
	if n == 1:
		return False

	if n > 2 and n % 2 == 0:
		return False

	max_divisor = math.floor(math.sqrt(n))
	for d in range(3, 1 + max_divisor, 2):
		if n % d == 0:
			return False

	return True

# testing out prime function
"""
for n in range(1, 21):
	print(n, is_prime_v3(n))"""

# timing prime function
t0 = time.time()
for n in range(1, 1000000):
	is_prime_v2(n)
	if n % 10000 == 0:		# print message every 10000 numbers so they know it's running
		print("{0}% Calculated".format(n/10000))
t1 = time.time()
print("Time required v3: ", t1 - t0)
