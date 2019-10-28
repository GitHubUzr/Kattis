'''This python program is meant to determine the 12 winners of a competition.
Team names come in order of rank and have the university they are representing.
A university can only have their top team counted as a winner.'''


# receives number of contestants
n = int(input())
winners = []
count = 0
# for every contestant
for x in range(n):
    # recive their university and team name
    uni,team = [str(word) for word in input().split()]
    # if the university already received an award, do nothing
    if uni in winners:
        pass
    # if university has not received award yet, add uni name to list of winners
    else:
        winners.append(uni)
        # print the university and associated team
        print(uni,team)
        # keep track of the # of winners
        count += 1
        # once 12 teams are awarded stop looping
        if count >= 12:
            break
