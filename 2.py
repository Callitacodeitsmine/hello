sub1 = int(input("Enter marks in subject 1: "))
sub2 = int(input("Enter marks in subject 2: "))
sub3 = int(input("Enter marks in subject 3: "))
sub4 = int(input("Enter marks in subject 4: "))
sub5 = int(input("Enter marks in subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
percentage = (total / 500) * 100
print("Total:", total)
print("Average:", average)
print("Percentage:", round(percentage, 2), "%")