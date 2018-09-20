# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for i in range(0, len(quote)):
#     if quote[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         print(quote[i])

# WAP to print all the numbers that are between 0 and 100 and divisible by 7

# for i in range(0, 100, 7):
#       if i%7 == 0:
#         print(i)

# Modify this loop to stop when i is exactly divisible by 11
# for i in range(0, 100, 7):
#         print(i)
#         if i>0 and i % 11 == 0:
#             break

# for i in range(0, 21):
#     if i > 0 and i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number
print(answer)
