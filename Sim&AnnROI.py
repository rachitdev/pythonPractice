from math import sqrt

p = float(input("amount invested: "))
t = float(input("period of investment: "))
r = float(input("rate of interest: "))

sInt = p*t*r/100
annualized_value  = p*((1+(0.01*r)) ** t)

print("Simple Rate of Return = %f" % (sInt))
print(round(annualized_value,2))

# if r > 0:
#     # Number of roots in this case are 2.
#     x1 = (((-b) + sqrt(r))/(2*a))
#     x2 = (((-b) - sqrt(r))/(2*a))
#
#     print(round(x1))
#     print(round(x2))
#
# elif r == 0:
#     # Number of roots in this case is 1.
#     x = (-b) / 2*a
#     print(round(x))
# else:
#     # No roots are obtained in this case.
#     print("Imaginary Number")
# exit()