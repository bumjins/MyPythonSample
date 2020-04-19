from random import *
from random import shuffle

user = []

for u in range(1, 21):
    user.append(u)

print(user)
shuffle(user)


winners = sample(user, 1)
del user[user.index(winners[0])]

for u in range(3):
	shuffle(user)
	winner = sample(user, 1)[0]
	winners.append(winner)
	del user[user.index(winner)]

print("--당첨자 발표 --")
print("치킨 당첨차 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("--축하합니다. --")

print(user)

#print(sample(shuffle_user, 1))
#print(got_chicken)
#users = range(1, 21)
#users = list(users)


