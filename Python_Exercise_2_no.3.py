## Exercise 2 - Number 3 ##
temp_f = eval(input("Enter the temparature in Fahrenheit : "))

t = 0

while t < 1:
    if -58 < temp_f < 48:
        wind = eval(input("Enter the wind speed in miles per hour : "))
        break 
    else:
        print("Temperature must be between -58F and 41F")
        temp_f = eval(input("Please re-enter the temperature in Fahrenheit : "))

while t < 1:
    if wind >=2:
        formula = 35.74 + (0.6215 * temp_f) - (35.75 * wind ** 0.16) + 0.4275 * temp_f * (wind ** 0.16)
        print("The wind chill index is ", format(formula, '.3f'))
        break
    else:
        print("Speed must be greater than or equal to 2")
        wind = eval(input("Please re-enter the wind speed miles per hour : "))
##