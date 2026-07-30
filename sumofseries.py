n = int(input("Enter n: "))
fact = 1
sum_series = 1
for i in range(1, n + 1):
    fact *= i
    sum_series += 1 / fact
print("Sum =", sum_series)
