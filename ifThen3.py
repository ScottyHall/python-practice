# Scalene triangle: All sides have differnet lengths
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
	print("This is a Scalene triangle.")
elif a == b and b == c:
	print("This is an Equilateral triangle.")
else:
	print("This is an Isosceles triangle.")

