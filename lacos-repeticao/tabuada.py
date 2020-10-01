"""
1. usando while
"""
n = int(input("De qual número você quer a tabuada? "))
#setar variável contadora
i = 1 
while i <= 10:
    print("{} x {} = {}".format(n, i, n*i))
    i = i + 1

