''' This python code is meant to answer 'yes'
if each word is unique and answer no if there
are duplicates of a word for an inputted string (all caps)
'''

def no_duplicates(my_list):
    # compares the number of words th the number of unique words
    # if total words = unique words, then duplicates is False
    if len(my_list) == len(set(my_list)):
        return False
    # if total words does not equal # unique words, then duplicates is True
    else:
        return True
    
# break the line into each word and put into list n
n = [str(word) for word in input().split()]
# calls the function no_duplicates
my_answer = no_duplicates(n)
# if duplicates is True
# then answer for 'were all the words unique' is 'no'
if my_answer:
    print("no")
# if duplicates is False
# then answer for 'were all the words unique' is 'yes'
else:
    print("yes")
