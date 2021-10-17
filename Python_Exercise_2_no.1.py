## Exercise 2 - Number 1 ##
import math

gravity = 9.8
mass = eval(input("Enter the mass of the cart (in kg) : "))
force = eval(input("Enter the force to pus the cart (in N) : "))

sinTh = (force / (mass * gravity))

Th = math.asin(sinTh)
dg = math.degrees(Th)

print("The angle of the ramp is : ", format(dg, '.1f'))
##