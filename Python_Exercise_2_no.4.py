## Exercise 2 - Number 4 ##
packages = eval(input("Enter the number of packages purchased : "))

ret_price = packages * 99

if packages >= 10 and packages <= 19:
    result_1 = ret_price - (10 * ret_price / 100)
    result1 = (10 * ret_price / 100)
    print("Discount amount @ 10% : $ ", format(result1, '.2f'))
    print("Total amount : $ ", format(result_1, '.2f'))
elif packages >= 20 and packages <= 49:
    result_2 = ret_price - (20 * ret_price / 100)
    result2 = (20 * ret_price / 100)
    print("Discount amount @ 20% : $ ", format(result2, '.2f'))
    print("Total amount : $ ", format(result_2, '.2f'))
elif packages >= 50 and packages <= 99:
    result_3 = ret_price - (30 * ret_price / 100)
    result3 = (30 * ret_price / 100)
    print("Discount amount @ 30% : $ ", format(result3, '.2f'))
    print("Total amount : $ ", format(result_3, '.2f'))
elif packages >= 100:
    result_4 = ret_price - (40 * ret_price/ 100)
    result4 = (40 * ret_price / 100)
    print("Discount amount @ 40% : $ ", format(result4, '.2f'))
    print("Total amount : $ ", format(result_4, '.2f'))
else:
    print("Discount amount @ 0% : $ 0.00 ")
    print("Total amount : $ ", format(ret_price, '.2f'))
##