from math import tan, pi

side = float(input("Please enter the length of the sides of your polygon: "))
number_of_sides = int(input("Please enter the number of sides of your polygon: "))

area = (number_of_sides * side ** 2) / (4 * tan(pi / number_of_sides))

print("The area of your polygon is", round(area, 2), "units")