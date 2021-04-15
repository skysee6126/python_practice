from random import *

users = range(1, 21)
users = list(users)
shuffle(users)

winners = sample(users, 4)
print ("1st winner: {0}".format(winners[0]))
print ("2nd winner: {0}".format(winners[1:]))