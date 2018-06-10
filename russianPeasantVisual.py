# Russian Peasant algorithm practice
import math

class Calculate():
	"""Prompts user for 2 numbers to multiply using the 'Russian Peasant Algorithm'"""
	def __init__(self):
		print("Welcome to the Russian Multiplication program.\nYou can multiply 2 numbers together.\n\n")
		x = int(input("First number: "))
		y = int(input("Second number: "))
		self.multiply(x, y)

	# multiply method accepts 2 ints, saves all 'y' pairs if x is odd, adds up all those 'y' values from the appended list
	def multiply(self, x, y):
		# originalx, y for equation output at finish
		originalx = x
		originaly = y
		# used for table output and should never be rounded
		unroundedx = 0
		# saves all 'y' values that correspond to an odd 'x' value (Added up for answer)
		addedList = [0]
		# rounded int number for visual output
		visualList = ""
		# character to represent visual output of numbers
		printCharacter = "* "
		splitCount = 0
		# if 'x' is odd, save the 'y' value to the list. These will be added to find the answer.
		if x%2 != 0:
			addedList = [y]
		while x != 1:
			x = x/2
			if x != originalx:
				unroundedx = unroundedx/2
			y = y*2
			if splitCount == 0:
				print("_Table__|__all_splits_are_valid_equations_")
				unroundedx = x
			splitCount += 1
			print("Split:" + str(splitCount) + " | " + str(unroundedx) + " * " + str(y) + " |")
			vx = int(x)
			vy = int(y)
			if originalx < 51 and originaly < 51:
				for i in range(vy):
					visualList = printCharacter+visualList
				for i in range(vx):
					print(visualList)

			

			if x == 1:
				addedList.append(y)
				break

			# needs to be a round number, but never round up
			x = x - 0.1		# prevents from rounding up
			x = round(x)


			if x%2 != 0:
				addedList.append(y)


		
		#for i in range(vx):
		#	visualList.append(printCharacter)
		#for i in range(vy):
		#	print(visualList)


		if x == 1:
			answer = 0
			for number in addedList:
				answer = answer + number
				#print("Number = " + str(number))
				#print("Answer = " + str(answer))
			print("\n'Y' values that are paired to an odd 'X' value: " + str(addedList))

			print("\n{0} * {1} = {2}".format(originalx, originaly, answer))


Calculate()