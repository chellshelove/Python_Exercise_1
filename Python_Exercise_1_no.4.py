## Exercise 1 - Number 4 ##
import math 

s = eval(input("Enter the side length of the hexagon : "))
area = (3 * math.sqrt(3)) * (s**2) / 2

print("The are of a hexagon with side lenght ", s , "is", format(area, '.3f'))
##