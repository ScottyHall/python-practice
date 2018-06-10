# fibonacci sequence, recursion and memoization
# python practice
# memoization == cached values for recursive functions
import timeit
from functools import lru_cache
# 1, 1, 2, 3, 5, 8, 13, 21
# first two are 1
# each term is sum of previous 2 terms

# goal is to write a function to return the nth value of the sequence
@lru_cache(maxsize = 10000)
def fibonacci(n):
	# check for valid input
	if type(n) != int:
		raise TypeError("n must be a positive int")
	if n < 1:
		raise ValueError("n must be a positive int")

	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)

def fib():
	fibNumber = int(input("What fibonacci sequence number do you wish to find?: "))
	print(fibonacci(fibNumber))

#memoization explicitly
fibonacci_cache = {}

def fibonacci_2(n):
	
	# if the cached value is present, return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	# compute the Nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci_2(n-1) + fibonacci_2(n-2)

	# cache the value and return it
	fibonacci_cache[n] = value
	return value

def fib_loop():
	for n in range(1, 501):
		fibonacci_2(n)
		if n == 500:
			print(n, ":", fibonacci_2(n))	# prints both the sequence you are on, and the value

fib()
"""
# time the optimized loop
print("optimized")
print(timeit.timeit("fib_loop()", setup="from __main__ import fib_loop", number=1))
print("Auto Cached")
print(timeit.timeit("fib()", setup="from __main__ import fib", number=1))
"""

