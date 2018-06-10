# Collect string / test length
""" A program to test input length of strings """

while True:
	# get user input string
	userInput = input("Please enter a test string: ")

	if len(userInput) < 6:
		print("Your string is too short.")
		print("Please enter a string with at least 6 characters.\n")
	else:
		print("'{0}', is accepted because it is '{1}' characters in length".format(userInput, len(userInput)))
		break
print("\nProgram Complete \n")

