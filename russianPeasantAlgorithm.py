# Russian Peasant algorithm practice
import math


def multiply(x, y):
	originalx = x
	originaly = y
	addedList = [0]
	visualList = []
	printCharacter = "* "
	if x % 2 != 0:
		addedList = [y]
	while x != 1:
		x = x / 2
		y = y * 2
		vx = int(x)
		vy = int(y)
		if x == 1:
			addedList.append(y)
			break

		x = x - 0.1
		x = round(x)
		print("x = " + str(x))
		print("y = " + str(y))
		if x % 2 != 0:
			addedList.append(y)

		
		#for i in range(vx):
		#	visualList.append(printCharacter)
		#for i in range(vy):
		#	print(visualList)

	if x == 1:
		answer = 0
		for number in addedList:
			answer = answer + number
			print("Number = " + str(number))
			print("Answer = " + str(answer))
		print("\n{0} * {1} = {2}".format(originalx, originaly, answer))
		print(addedList)
		


def input_numbers():
	print("Welcome to the Russian Multiplication program.\nYou can multiply 2 numbers together.\n\n")
	x = int(input("First number: "))
	y = int(input("Second number: "))
	multiply(x, y)

input_numbers()