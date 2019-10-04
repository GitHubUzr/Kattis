'''
This python code is meant to receive an encrypted message
and after splitting the message in half (Divide), summing up the
alphabet index values of each half and shifting them by the
calculated value (Rotate), and finally shifting each character
in the first half by the index value of the corresponding character
in the second half (Merge) will it decrypt the message.

'''
# this function shifts the letters in the string by the specified amount
def cipher(strin,shift):
    moved = ""
    for ch in strin:
        moved += chr((ord(ch)+shift-65) % 26+65)
    return moved

import string
import sys

# receiving input as string
x = str(input())
test_list =[]
test_list = list(string.ascii_uppercase)

# creating an uppercase list of the alphabet
rotate1 = 0
rotate2 = 0
shift = 0

# splits the input string in half
first = x[0:len(x)//2]
second = x[len(x)//2:]

# calculates the rotation value for the two new strings
for i in first:
    for j in test_list:
        if i == j:
            rotate1 += test_list.index(j)

for i in second:
    for j in test_list:
        if i == j:
            rotate2 += test_list.index(j)


rotated_string = ""
merge_shifts = []
test_string = ""
# calls upon the function above to shift each string by its rotation value
rotated_string = cipher(first,rotate1)
test_string = cipher(second,rotate2)
# places the index value of each character in the second string into a list
for ar in test_string:
    for ac in test_list:
        if ar == ac:
            merge_shifts.append(test_list.index(ac))
count = 0
merge_string = ""
# shifts each character in the first string by the value from the second string 
for ter in rotated_string:
    merge_string += chr((ord(ter)+merge_shifts[count]-65) % 26+65)
    count += 1
# prints the decrypted message
print(merge_string)

