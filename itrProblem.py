string = "1234567890"

my_itr = iter(string)
print(my_itr)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))

for i in range(0, len(string)):
    print(string[i])