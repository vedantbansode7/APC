import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))
is_prime = True
if root < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(root)) + 1):
        if root % i == 0:
            is_prime = False
            break
print("Square root =", root)
if is_prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
