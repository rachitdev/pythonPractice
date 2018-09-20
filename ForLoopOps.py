# for i in range(0,20):
#     print (i)

# The Following program will extract each letter/integer of a string

num = "224,098,897,456,334,223,190,389,268"
cleanedNum = ''
for i in range(0, len(num)):
    if num[i] in '0123456789':
        cleanedNum = cleanedNum + num[i]
print(cleanedNum)