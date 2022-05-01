import random
#this code determs who wins

teamA = 1
teamB = 2
Awin = 0
Bwin =0
x = 1
while x != 1000:
    battle = (random.randint(1,6))

    if battle <= 3:
        print("#############")
        print("b win")
        Bwin += 1
    else:
        print("#############")
        print("a win")
        Awin += 1
    x += 1



print("a won this many times:{}".format(Awin))
print("B won this many times:{}".format(Bwin))
