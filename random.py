import random

users = range(1, 21)
users = list(users)
random.shuffle(users)

winners = random.sample(users, 4)
print ("1st winner: {}".format(winners[0]))
print ("2nd winner: {}".format(winners[1:]))