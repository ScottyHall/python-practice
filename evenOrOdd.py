# Prompt user to enter number / test if even or odd

userInput = input("Please enter an integer: ")
number = int(userInput)

if number %2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")