# function writing practice to illustrate reusing logic
import math

def ping():
	return "Ping!"

x = ping()
print(x)

def sphere_volume(r):
	"""Returns the volume of a sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v

print("The volume of a sphere with a radius of '2' = {0}".format(sphere_volume(2)))

def triangle_area(b, h):
	"""Returns the area of a triangle with base 'b' and height 'h'."""
	return 0.5 * b * h

print("The area of a triangle with a base of '3' and height of '6' = {0}".format(triangle_area(3, 6)))


# KEYWORD ARGUMENTS
#default arguments
def cm(feet = 0, inches = 0):
	"""Converts a length from feet and inches to centimeters."""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm

print("'5' feet = {0}cm".format(cm(feet = 5)))
print("'70' inches = {0}cm".format(cm(inches = 70)))
print("'5' feet, '8' inches = {0}cm".format(cm(feet = 5, inches = 8)))

# keyword arguments vs required arguments
# keyword arguments must be defined last
# keyword arguments have a default value
