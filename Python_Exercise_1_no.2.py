## Exercise 1 - Number 2 ##
v = eval(input("Enter the plane's take off speed in m/s : "))
a = eval(input("Enter the plane's acceleration in m/s**2 : "))
formula = (v**2) / (2*a)

print("The minimum runway length needed for this airplane is : ", format(formula, '.4f'))
##