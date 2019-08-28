
input_list = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
letter_input_list = list(map(list, input_list))
i = len(letter_input_list)
count = 0
for a in range(0,i):
    if "S" == letter_input_list[a][0]:
        count = count+1
print(count)