age = 35
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("My age is %d years" % age)
print("My age is %d %s %s %d %s" % (age, "years", "and", 10, "months"))
for i in range(1, 13):
    print("Number %d has a square %4d and a cube %4d" % (i, i**2, i**3))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])