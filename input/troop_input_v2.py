
import numpy as np
#these troops are aliged [strenght, cost, team list position]
rifleman = [1, 1, 0]
gunner = [2, 2, 1]
sniper = [3, 2.5, 2]
medic = [4, 3, 3]
tank = [7, 6, 4]

active_point = ""

#tank bonus
########[r,g,s,m,t]
#########0 1 2 3 4 list pos
pointA = [0,0]
pointB = [0,0]
pointC = [0,0]

teamB = [0,0,0,0,0]
teamA = [0,0,0,0,0]

teamA_pointA = [0,0,0,0,0]
teamA_pointB = [0,0,0,0,0]
teamA_pointC = [0,0,0,0,0]

teamB_pointA = [0,0,0,0,0]
teamB_pointB = [0,0,0,0,0]
teamB_pointC = [0,0,0,0,0]


teamA_power = 0
teamB_power = 0
pointA_owner = ""
pointB_owner = ""
pointC_owner = ""

#different troops
dif_troops = [rifleman, gunner, sniper, medic, tank]
budget = int(input("budget per team:"))
teamA_budget = budget
teamB_budget = budget
print("you budget is {}".format(budget))

#checks input for letters
def intcheck(team_def2, num_check_point):
    
    valid = False
    while not valid:
        error = ("whoops! please enter a correctly formated input")

        try:
            intcheck_response = input("{} please enter how many troops you would like to send to point {}:".format(team_def2, num_check_point))
            # makes 1 into 00001
            intcheck_response_len = len(str(intcheck_response))
            if intcheck_response_len == 5:
                return intcheck_response
            else:
                print(error)
                print()

        except ValueError:
            print(error)
#you u dummy 
def troop_costs():
    print("rifleman is $1 and 1 power")
    print("gunner is $2 and 2 power")
    print("sniper is $2.5 and 3 power")
    print("medic is $3 and 4 power")
    print("tank is $6and 7 power")
    print("please format your input like this:")
    print(" x(rifleman) x(gunner)x (sniper) x(medic) x(tank)")
    print(" so if you wanted 1 rifleman 2gunner 1sniper 2 medic 1 tank")
    print("it would go like this: 12121")
    print("or if you wanted 1 soldier it would look like this:10000")
    print("REMBER YOU HAVE 3 TEAMS TO SPEND MONEY ON.")

######team a troop selection
def troop_choose(team_def,select_point_def):
    global teamA
    global teamB
    global teamA_budget
    global teamB_budget
    global pointA 
    global pointB 
    global pointC
    global teamA_pointA
    global teamA_pointB
    global teamA_pointC

    global teamB_pointA
    global teamB_pointB
    global teamB_pointC
    enter_loop = "x"
            #input loop alos changes from num to list
    while enter_loop != "":
        raw_troop_input_def = intcheck(team_def,select_point_def)
        troop_input_def = [int(i) for i in str(raw_troop_input_def)]
        print("so you would like {} rileman {} gunner {} sniper {} medic and {} tank to point {}".format(troop_input_def[0], troop_input_def[1], troop_input_def[2], troop_input_def[3], troop_input_def[4], select_point_def))
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
    
    #determs where to send result eg:what point and what team 
    if select_point_def == "A":
          
        if team_def == "teamA":################################working here on point troops
            pointA[0] = troop_input_def
            teamA_budget -= troop_def_total
            for i in range(0,5):
                teamA_pointA[i] = teamA_pointA[i]+troop_input_def[i]
        elif team_def == "teamB":
            pointA[1] = troop_input_def
            teamB_budget -= troop_def_total
            for i in range(0,5):
                teamB_pointA[i] = teamB_pointA[i]+troop_input_def[i]
    elif select_point_def == "B":
          
        if team_def == "teamA":################################working here on point troops
            pointB[0] = troop_input_def
            teamA_budget -= troop_def_total
            for i in range(0,5):
                teamA_pointB[i] = teamA_pointB[i]+troop_input_def[i]
        elif team_def == "teamB":
            pointB[1] = troop_input_def
            teamB_budget -= troop_def_total
            for i in range(0,5):
                teamB_pointB[i] = teamB_pointB[i]+troop_input_def[i]
        
    elif select_point_def == "C":
          
        if team_def == "teamA":################################working here on point troops
            pointC[0] = troop_input_def
            teamA_budget -= troop_def_total
            for i in range(0,5):
                teamA_pointC[i] = teamA_pointC[i]+troop_input_def[i]
            
        elif team_def == "teamB":
            pointC[1] = troop_input_def
            teamB_budget -= troop_def_total
            for i in range(0,5):
                teamB_pointC[i] = teamB_pointC[i]+troop_input_def[i]
    else:
        print("error at choosing point input")

    

troop_costs()
troop_choose("teamA", "A")
print("team A  point A")
print("you have ${} left".format(teamA_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointA[0], teamA_pointA[1], teamA_pointA[2], teamA_pointA[3], teamA_pointA[4]))
print("####################################################################")

troop_choose("teamA", "B")
print("team A  point b")
print("you have ${} left".format(teamA_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointB[0], teamA_pointB[1], teamA_pointB[2], teamA_pointB[3], teamA_pointB[4]))
print("####################################################################")

troop_choose("teamA", "C")
print("team A  point c")
print("you have ${} left".format(teamA_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointC[0], teamA_pointC[1], teamA_pointC[2], teamA_pointC[3], teamA_pointC[4]))
print("####################################################################")




troop_choose("teamB", "A")
print("TEAM B point A")
print("you have ${} left".format(teamB_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointA[0], teamB_pointA[1], teamB_pointA[2], teamB_pointA[3], teamB_pointA[4]))
print("####################################################################")

troop_choose("teamB", "B")
print("TEAM B point b")
print("you have ${} left".format(teamB_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointB[0], teamB_pointB[1], teamB_pointB[2], teamB_pointB[3], teamB_pointB[4]))
print("####################################################################")

troop_choose("teamB", "C")
print("TEAM B point c")
print("you have ${} left".format(teamB_budget))
print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointC[0], teamB_pointC[1], teamB_pointC[2], teamB_pointC[3], teamB_pointC[4]))
print("####################################################################")


print(teamA_pointA, teamA_pointB, teamA_pointC, teamB_pointA, teamB_pointB, teamB_pointC)
