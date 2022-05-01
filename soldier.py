
rifleman = [1,1]
gunner = [2,2.5]
sniper = [3,4]
medic = [1,3]
tank = [6,7]
print("hi this is a tank game")
print("please format you team")
print("to format you team is")
print(" x(rifleman) x(gunner)x (sniper) x(medic) x(tank)")
print(" so if you wanted 1 rifleman 2gunner 1sniper 2 medic 1 tank")
print("it would go like this: 12121 this number must ad up to 10 or below")
x1 = 1 
while x1 == 1:
    raw_input1 =  input("so please enter you number:")
    team = [int(i) for i in str(raw_input1)]
    teamadd = sum(team)
    if teamadd < 11:
        print("Whoops, You choose too many troops. Try again")
    else:
        x = 2
        


print("so you would like {} rileman {} gunner {} sniper {} medic and {} tank".format(team[0], team[1], team[2], team[3], team[4]))
      
