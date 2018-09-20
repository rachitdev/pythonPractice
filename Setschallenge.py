string_input = input(print("Enter a string: "))
vowels = frozenset("aeiouAEIOU")

finalSet = set(string_input).difference(vowels)
print(sorted(finalSet))
newStr = ""
for char in sorted(finalSet):
    print(char)
    newStr += char
print(newStr)
