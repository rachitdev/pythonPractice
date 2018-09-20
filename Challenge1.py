print("Enter Name ")
name = input()
print("Enter Age")
age = int(input())

if 18 <= age < 31:
    print("Welcome %s, enjoy the party." % name)
else:
    print("Sorry %s, You are not eligible." % name)