a=int(input("Enter num A: "))
b=int(input("Enter num B: "))
c=int(input("Enter num C: "))
if a>b and a>c:
    print("A is largest")
elif b>a and b>c:
    print("B is largest")
else:
    print("C is largest")

if a<b and a<c:
    print("A is smallest")
elif b<a and b<c:
    print("B is smallest")
else:
    print("C is smallest")
