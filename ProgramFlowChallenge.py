ipa = input("Enter the IP Address: ")
segment = 1
segment_length = 0

for character in ipa:
    if character == '.':
        print("The {} line segment has characters {}".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
if character != '.':
        print("The {} line segment has characters {}".format(segment, segment_length))