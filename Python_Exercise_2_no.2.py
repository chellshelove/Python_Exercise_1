## Exercise 2 - Number 2 ##
edge_1 = eval(input("Enter length of edge 1 : "))
edge_2 = eval(input("Enter length of edge 2 : "))
edge_3 = eval(input("Enter length of edge 3 : "))

perimeter = edge_1 + edge_2 + edge_3

if edge_1 + edge_2 > edge_3 and edge_1 + edge_3 > edge_2 and edge_2 + edge_3 > edge_1:
    print("The perimeter is : ", perimeter)
else:
    print("Perimeter cannot be calculated: the input is inavlid. ")
##

## Exercise 2 - Number 3 ##

##

## Exercise 2 - Number 4 ##
packages = eval(input("Enter the number of packages purchased : "))
disc_amnt = eval(input("Discount amount :"))