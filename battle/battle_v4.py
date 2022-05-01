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
def power_cal(team_power_def):
    global teamA_power
    global teamB_power
    global teamA
    global teamB
    if team_power_def == "teamA":
        teamA_power = teamA[0]*1 + teamA[1]*2 + teamA[2]*3 + teamA[3]*4 + teamA[4]*7

    elif team_power_def == "teamB":
        teamB_power = teamB[0]*1 + teamB[1]*2 + teamB[2]*3 + teamB[3]*4 + teamB[4]*7
    
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
    
    if def_point == "A":
        print("-----------------------------------------------------------------------")
        print("                           BATTLE AT POINT B")
        
        if teamA_pointA > teamA_pointA:
            dif = teamA_pointA - teamA_pointA
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            troop_half("A", "B")
            pointA_owner = "teamA"
            
        elif teamB_pointA > teamA_pointA:
            dif = teamb_pointA - teamA_pointA
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            troop_half("A", "A")
            pointA_owner = "teamB"
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                troop_half("A", "B")
                pointA_owner = "teamB"
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                troop_half("A", "A")
                pointA_owner = "teamB"

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointA = [0,0,0,0,0]
                teamB_pointA = [0,0,0,0,0]
    print("-----------------------------------------------------------------------")
    elif def_point == "B":
        print("                           BATTLE AT POINT B")
        
        
        if teamA_pointB > teamA_pointB:
           print("-----------------------------------------------------------------------")
            dif = teamA_pointB - teamA_pointB
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            troop_half("B", "B")
            pointB_owner = "teamA"
            
        elif teamB_pointB > teamA_pointB:
            dif = teamb_pointB - teamA_pointB
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            troop_half("B", "A")
            pointB_owner = "teamB"
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                troop_half("B", "B")
                pointB_owner = "teamB"
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                troop_half("B", "A")
                pointB_owner = "teamB"

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointB = [0,0,0,0,0]
                teamB_pointB = [0,0,0,0,0]
    print("-----------------------------------------------------------------------")
    elif def_point == "C":
        print("-----------------------------------------------------------------------")
        print("                           BATTLE AT POINT C")
        if teamA_pointC > teamA_pointC:
            dif = teamA_pointC - teamA_pointC
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            troop_half("C", "B")
            pointC_owner = "teamA"
            
        elif teamB_pointC > teamA_pointC:
            dif = teamb_pointC - teamA_pointC
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            troop_half("C", "A")
            pointC_owner = "teamB"
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                troop_half("C", "B")
                pointC_owner = "teamB"
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                troop_half("C", "A")
                pointC_owner = "teamB"

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointC = [0,0,0,0,0]
                teamB_pointC = [0,0,0,0,0] 
    print("-----------------------------------------------------------------------")
