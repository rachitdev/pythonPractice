import os

file_path = os.getcwd() + "\sample.txt"
gibberish = open(file_path)

# for lines in gibberish:
#     print(lines)

# Using readlines to read the contents of the file
# line = gibberish.readline()
# while line:
#     print(line, end='')
#     line = gibberish.readline()

# returning a list of lines in the whole poem
lines = gibberish.readlines()
print(lines)

gibberish.close()