import sys

fruits = {"apple": "Good for making cider", "guava": "A sweet fruit with lot of seeds",
          "orange": "A sweet citrus fruit", "banana": "A fruit rich in vitamins and iron"}

print(fruits)
print(fruits.get("guava"))
fruits["lemon"] = "A citrus fruit rich with vitamin c"  #Adding an another key value pair in the dictionary.

# fruits_key = input("Enter the fruit name: ")
#
# if fruits_key == "quit":
#     sys.exit()
# if fruits_key in fruits:
#     desc = fruits.get(fruits_key)
#     print(desc)
# else:
#     print("I don't have this fruit information.")

# Printing keys with their respective values
# ordered_keys = sorted(fruits.keys())
# print('_' * 60)
# for f in ordered_keys:
#     print(f + " - " + fruits[f])
#     print('_' * 60)

# Converting the dictionary to a tuple
fruits_tuple = tuple(fruits.items())
print(fruits_tuple)
print(dict(fruits_tuple))  # Converting the tuple back to dictionary
for f in fruits_tuple:
    item, description = f
    print(item + " - " + description)

# Converting the dictionary to a list
fruits_list = list(fruits.items())
print(fruits_list)
print(dict(fruits_list))  # Converting the list back to dictionary
for f in fruits_list:
    item, description = f  # Unpacking the tuples inside the list.
    print(item + " is " + description)

# del fruits["orange"]  # Deletes the key value pair with the key "orange".
# print(fruits)
# fruits.clear()        # Clears the whole dictionary.
# print(fruits)