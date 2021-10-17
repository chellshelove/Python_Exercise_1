## Exercise 1 - Number 3 ##
subt = eval(input("Enter the subtotal : $"))
tip_perc = eval(input("Enter the percantage (as a %) : "))
tip_amnt = subt * (tip_perc / 100)

print("Subtotal : $ ", format(subt, ',' '.2f'))
print("Tip : $ ", format(tip_amnt, '.2f'))
print("Total : $ ", format(subt + tip_amnt, '.2f'))
##