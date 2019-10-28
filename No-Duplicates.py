''' This python code is meant to answer 'yes'
if each word is unique and answer no if there
are duplicates of a word for an inputted string (all caps)
'''

# break the line into each word and put into list n
n = [str(word) for word in input().split()]
# create a blank list m ; this will all the unique words
m = []
# set word repeated to false
word_repeated = False

# look at each word in the list
for x in n:
    # if the word is already in the list
    if x in m:
        # set word repeated to true
        word_repeated = True
        # and end the loop
        break
    # if word is not in the list
    else:
        # add it to the list
        m.append(x)
        
# if word repeated was set to True
# then answer for 'were all the words unique' is 'no'
if word_repeated:
    print("no")
# if word repeated stayed false
# then answer for 'were all the words unique' is 'yes'
else:
    print("yes")
