a = [2, 4, 6, 8]
b = [1, 3, 5, 7, 9]
rev_a = a.reverse()
rev_b = b.reverse()
print(rev_a)
print(rev_b)
a.append(10)
b.append(11)
c = a + b
print(c)
print(sorted(c))

nums = [a, b]
print(nums)
for items in nums:
    print(items)
    for values in items:
        print(values)