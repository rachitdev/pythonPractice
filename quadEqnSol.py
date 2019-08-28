from math import sqrt

a = float(input("an integer, a – Coefficient of x^2: "))
b = float(input("an integer, b – Coefficient of x: "))
c = float(input("an integer, c – Constant term: "))

r = b**2 - 4*a*c
# print (r)

if r > 0:
    # Number of roots in this case are 2.
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))

    print(round(x1))
    print(round(x2))

elif r == 0:
    # Number of roots in this case is 1.
    x = (-b) / 2*a
    print(round(x))
else:
    # No roots are obtained in this case.
    print("Imaginary Number")
exit()