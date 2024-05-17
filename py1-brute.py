import sys
# For the brute force solution of the problem,  used top-down recursive procedure.

def rod_cutting(price, length):
    if length <= 0:
        return 0
    max_val = -sys.maxsize -1
    for i in range(length):
        max_val = max(max_val, price[i] + rod_cutting(price, length - (i + 1)))
        # continuous loop till length is equal or less than 0. Will fetch the max price and store it into max_val. 
    return max_val

# price = [3, 5, 8, 9, 10, 17, 17, 20]
length = int( input("Enter rod's length : "))
price = []
print("Input the value of cuttings : ")
for j in range(0, length):
    val = int( input())
    price.append(val)

print("Maximum obtainable value : " , rod_cutting(price, length))