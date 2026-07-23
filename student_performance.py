sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
total = sub1 + sub2 + sub3
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)
if average >= 75:
    print("Grade: A")
    print("Remark: Excellent")
elif average >= 60:
    print("Grade: B")
    print("Remark: Good")
elif average >= 40:
    print("Grade: C")
    print("Remark: Average")
else:
    print("Grade: D")
    print("Remark: Poor")
