a = 0
print(a)
b = 1
print(b)
n = 10
for i in range(0, n-2):
    c = a+b
    a = b
    b = c
    print(c)