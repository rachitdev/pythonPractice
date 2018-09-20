menu = ["potatoes", "tomatoes", "onions", "cucumbers", "beetroot", "lotus stem"]
n = len(menu)
my_itr = iter(menu)
for i in range(0, n):
    print(menu[i])
    print(my_itr) # This line returns the register / memory value.
    print(next(my_itr)) # This line is the same as the first print line, returns same thing.