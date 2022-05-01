import random
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

teamA_pointA = [0,0,0,0,3]
teamA_pointB = [0,0,0,0,2]
teamA_pointC = [0,0,0,0,2]

teamB_pointA = [0,0,0,0,2]
teamB_pointB = [0,0,0,0,2]
teamB_pointC = [0,0,0,0,2]


teamA_power = 0
teamB_power = 0
pointA_owner = ""
pointB_owner = ""
pointC_owner = ""

#different troops
def troop_half(team_half):
    for i in range(0,5):
        team_half[i] = team_half[i]*0.5
    return team_half

def power_cal(team_power_def):
    zoopyty_ploop = [0,0,0,0,0]
    zoopyty_ploop = team_power_def[0]*1 + team_power_def[1]*2 + team_power_def[2]*3 + team_power_def[3]*4 + team_power_def[4]*7
    return zoopyty_ploop

def battle(def_point):
    global teamA_power
    global teamB_power
    global teamA
    
    global teamB

    global teamA_pointA
    global teamA_pointB
    global teamA_pointC

    global teamB_pointA
    global teamB_pointB
    global teamB_pointC
    AA = power_cal(teamA_pointA)
    AB = power_cal(teamA_pointB)
    AC = power_cal(teamA_pointC)
    BA = power_cal(teamB_pointA)
    BB = power_cal(teamB_pointB)
    BC = power_cal(teamB_pointC)

    
    if def_point == "A":
        print("-----------------------------------------------------------------------")
        print("                           BATTLE AT POINT B")
        
        if AA > BA:
            dif = AA - BA
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            teamB_pointA = troop_half(teamB_pointA)
            pointA_owner = "teamA"
            
        elif BA > AA:
            dif = teamB_pointA - teamA_pointA
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            teamB_pointA = troop_half(teamA_pointA)
            pointA_owner = "teamB"
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                teamB_pointA = troop_half(teamB_pointA)
                pointA_owner = "teamB"
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                teamA_pointA = troop_half(teamA_pointA)
                pointA_owner = "teamB"

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointA = [0,0,0,0,0]
                teamB_pointA = [0,0,0,0,0]
        print("-----------------------------------------------------------------------")

    print(AA, AB, AC, BA, BB, BC)

battle("A")

print(teamA_pointA, teamA_pointB, teamA_pointC, teamB_pointA, teamB_pointB, teamB_pointC)

