import random as r

n = r.randint(1,6)
m = r.random()
rps = ['rock', 'paper', 'scissors']
z = r.choice(rps)

cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
r.shuffle(cards)



print(cards)
print(n)
print(m)
print(z)