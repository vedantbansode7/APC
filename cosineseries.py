import math
x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))
cosx = 1
sign = -1
for i in range(2, 2 * n, 2):
    cosx += sign * (x ** i) / math.factorial(i)
    sign *= -1
print("cos(x) =", cosx)
print("Actual value =", math.cos(x))
