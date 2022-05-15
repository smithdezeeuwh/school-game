def intcheck(team_def2):
    valid = False
    while not valid:
        error = ("whoops! please enter a correctly formated input")

        try:
            intcheck_response = int(input("{} please enter how many troops you would like:".format(team_def2)))
            # makes 1 into 00001
            intcheck_response_len = len(str(intcheck_response))
            if intcheck_response_len == 5:
                return intcheck_response
            else:
                print(error)
                print()

        except ValueError:
            print(error)
def troop_costs():
    print("rifleman is $1")
    print("gunner is $2")
    print("sniper is $2.5")
    print("medic is $3")
    print("tank is $6")
    print("please format your input like this:")
    print(" x(rifleman) x(gunner)x (sniper) x(medic) x(tank)")
    print(" so if you wanted 1 rifleman 2gunner 1sniper 2 medic 1 tank")
    print("it would go like this: 12121")
    print("or if you wanted 1 soldier it would look like this:10000")

#these troops are aliged [strenght, cost, team list position]
rifleman = [1, 1, 0]
gunner = [2, 2, 1]
sniper = [3, 2.5, 2]
medic = [4, 3, 3]
tank = [7, 6, 4]
#tank bonus
########[r,g,s,m,t]
#########0 1 2 3 4 list pos
teamA = [0,0,0,0,0]
#different troops
dif_troops = [rifleman, gunner, sniper, medic, tank]
budget = int(input("budget per team:"))
teamA_budget = budget
teamB_budget = budget
print("you budget is {}".format(budget))
######team a troop selection
def troop_choose(team_def):
    global teamA
    global teamB
    global teamA_budget
    global teamB_budget
    enter_loop = "x"

    while enter_loop != "":
        raw_troop_input_def = intcheck(team_def)
        troop_input_def = [int(i) for i in str(raw_troop_input_def)]
        print("so you would like {} rileman {} gunner {} sniper {} medic and {} tank".format(troop_input_def[0], troop_input_def[1], troop_input_def[2], troop_input_def[3], troop_input_def[4]))
        troop_def_total = troop_input_def[0]*1 + troop_input_def[1]*2 + troop_input_def[2]*2.5 + troop_input_def[3]*3 + troop_input_def[4]*6
        print(troop_def_total)
        #checks budget
        if team_def == "teamA":
            if troop_def_total > teamA_budget:
                print("you dont have enough money. You only have ${}".format(teamA_budget))
                print("please try again")
            else:
                enter_loop = input("please press enter to confirm")
        elif team_def == "teamB":
            if troop_def_total > teamB_budget:
                print("you dont have enough money. You only have ${}".format(teamb_budget))
                print("please try again")
            else:
                 enter_loop = input("please press enter to confirm")
    
    #determs where to send result
    if team_def == "teamA":
        teamA = troop_input_def
        teamA_budget -= troop_def_total
    else:
        teamB = troop_input_def
        teamB_budget -= troop_def_total
        

troop_costs()
troop_choose("teamA")
print("you have ${} left".format(teamA_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA[0], teamA[1], teamA[2], teamA[3], teamA[4]))

troop_choose("teamB")
print("you have ${} left".format(teamB_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB[0], teamB[1], teamB[2], teamB[3], teamB[4]))
