import random

#point    a b is the power on each side

pointA = [0,0]
pointB = [0,0]
pointC = [0,0]
teamB = [0,0,0,0,0]
teamA = [0,0,0,0,0]
teamA_power = 0
teamB_power = 0
pointA_owner = ""
pointB_owner = ""
pointC_owner = ""
rifleman = [1, 1, 0]
gunner = [2, 2, 1]
sniper = [3, 2.5, 2]
medic = [4, 3, 3]
tank = [7, 6, 4]

teamA_pointA = [0,0,0,0,0]
teamA_pointB = [0,0,0,0,0]
teamA_pointC = [0,0,0,0,0]

teamB_pointA = [0,0,0,0,0]
teamB_pointB = [0,0,0,0,0]
teamB_pointC = [0,0,0,0,0]

teamA_wins = 0
teamB_wins = 0

#this code halfs all values in team lists 
def troop_half(team_half):
    for i in range(0,5):
        if (team_half[i] % 2) == 0:
            team_half[i] = team_half[i]*0.5
        else:
            team_half[i] = team_half[i] - 1
            team_half[i] = team_half[i]*0.5
    return team_half
    
#calculats the power of each team
def power_cal(team_power_def):
    power_cal_def = [0,0,0,0,0]
    power_cal_def = team_power_def[0]*1 + team_power_def[1]*2 + team_power_def[2]*3 + team_power_def[3]*4 + team_power_def[4]*7
    return power_cal_def
#battle def
def battle(def_point):
    global teamA_power
    global teamB_power
    global teamA
    global teamB
    global teamA_wins
    global teamB_wins

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
        print("\n")
        print("-----------------------------------------------------------------------")
        print("                           BATTLE AT POINT A")
        
        if AA > BA:
            dif = AA - BA
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            teamB_pointA = troop_half(teamB_pointA)
            pointA_owner = "teamA"
            teamA_wins += 1
            
        elif BA > AA:
            dif = BA - AA
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            teamB_pointA = troop_half(teamA_pointA)
            pointA_owner = "teamB"
            teamB_wins += 1
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                teamB_pointA = troop_half(teamB_pointA)
                pointA_owner = "teamB"
                teamA_wins += 1
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                teamA_pointA = troop_half(teamA_pointA)
                pointA_owner = "teamB"
                teamB_wins += 1
                

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointA = [0,0,0,0,0]
                teamB_pointA = [0,0,0,0,0]
        print("-----------------------------------------------------------------------")
    elif def_point == "B":
        print("\n")
        print("                           BATTLE AT POINT B")
        
        
        if AB > BB:
            print("-----------------------------------------------------------------------")
            dif = AB - BB
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            teamB_pointB = troop_half(teamB_pointB)
            pointB_owner = "teamA"
            teamA_wins += 1
            
        elif BB > AB:
            dif = BB - AB
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            teamA_pointB = troop_half(teamA_pointB)
            pointB_owner = "teamB"
            teamB_wins += 1
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                teamB_pointB = troop_half(teamB_pointB)
                pointB_owner = "teamA"
                teamA_wins += 1
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                teamA_pointC = troop_half(teamA_pointC)
                pointB_owner = "teamB"
                teamB_wins += 1

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointB = [0,0,0,0,0]
                teamB_pointB = [0,0,0,0,0]
        print("-----------------------------------------------------------------------")
    elif def_point == "C":
        print("\n")
        print("-----------------------------------------------------------------------")
        print("                           BATTLE AT POINT C")
        if AC > BC:
            dif = AC - BC
            print("team A won the battle by {} power points".format(dif))
            print("team b had heavy casualites and lost half its troops.")
            teamB_pointC = troop_half(teamB_pointC)
            pointC_owner = "teamA"
            teamA_wins += 1
            
        elif BC > AC:
            dif = BC - AC
            print("team B won the battle by {} power points".format(dif))
            print("team a had heavy casualites and lost half its troops.")
            teamA_pointC = troop_half(teamA_pointC)
            pointC_owner = "teamB"
            teamB_wins += 1
        else:
            random_num = random.randint(0,3)
            if random_num == 1:
                print("the teams were even but by a stroke of luck TEAM A won")
                print("team b had heavy casualites and lost half its troops.")
                teamB_pointC = troop_half(teamB_pointC)
                pointC_owner = "teamA"
                teamA_wins += 1
        
            elif random_num == 2:
                print("the teams were even but by a stroke of luck TEAM B won")
                print("team a had heavy casualites and lost half its troops.")
                teamA_pointC = troop_half(teamA_pointC)
                pointC_owner = "teamB"
                teamB_wins += 1

            else:
                print("both teams fought hard but there was a tie and heavy caualtes")
                print("no troops remain on point a")
                teamA_pointC = [0,0,0,0,0]
                teamB_pointC = [0,0,0,0,0] 
    print("-----------------------------------------------------------------------") 
#cheack 00000 inputs            
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

#self explanitroy 
def troop_costs():
    print('''
    Welcome to the WW2 battle Field
    theses are the costs and power of different troops
    rifleman is $1 and 1 power
    gunner is $2 and 2 power
    sniper is $2.5 and 3 power
    medic is $3 and 4 power
    tank is $6and 7 power
    READ THE WHOLE THING PLEASE:
    please format your input like this:
     x(rifleman) x(gunner)x (sniper) x(medic) x(tank)
    so if you wanted 1 rifleman 2gunner 1sniper 2 medic 1 tank
    it would go like this: 12121")
    or if you wanted 1 soldier it would look like this:10000
    REMBER YOU HAVE 3 POINTS TO SPEND MONEY ON.
    \n
    ''')
#input for troops 
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
        print("that costs ", troop_def_total)
        
        #checks budget
        if team_def == "teamA":
            if troop_def_total > teamA_budget:
                print("you dont have enough money. You only have ${}".format(teamA_budget))
                print("please try again")
            else:
                enter_loop = input("please press enter to confirm")
        elif team_def == "teamB":
            if troop_def_total > teamB_budget:
                print("you dont have enough money. You only have ${}".format(teamB_budget))
                print("please try again")
            else:
                 enter_loop = input("please press enter to confirm")
    
    #determs where to send result eg:what point and what team 
    if select_point_def == "A":
          
        if team_def == "teamA":
            pointA[0] = troop_input_def
            teamA_budget -= troop_def_total
            for i in range(0,5):
                teamA_pointA[i] = teamA_pointA[i]+troop_input_def[i]
        elif team_def == "teamB":
            pointA[1] = troop_input_def
            teamB_budget -= troop_def_total
            for i in range(0,5):
                teamB_pointA[i] = teamB_pointA[i]+troop_input_def[i]
        else:
            print("error at point A team")
    elif select_point_def == "B":
          
        if team_def == "teamA":
            pointB[0] = troop_input_def
            teamA_budget -= troop_def_total
            for i in range(0,5):
                teamA_pointB[i] = teamA_pointB[i]+troop_input_def[i]
        elif team_def == "teamB":
            pointB[1] = troop_input_def
            teamB_budget -= troop_def_total
            for i in range(0,5):
                teamB_pointB[i] = teamB_pointB[i]+troop_input_def[i]
        else:
            print("error at point b team")
    elif select_point_def == "C":
          
        if team_def == "teamA":
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
            print("error at point C team")

    else:
        print("error at choosing point input")
def clear():
    for i in range(30):
        print("##############################################################################################################################################\n")
    


troop_costs()
dif_troops = [rifleman, gunner, sniper, medic, tank]
budget = int(input("budget per team:"))

round_money = int(input("how much money would you like per round:"))
many_round = int(input("how many rounds do you want:"))

teamA_budget = budget
teamB_budget = budget
print("your budget per tean is {}".format(budget))


print(teamA_pointA, teamA_pointB, teamA_pointC, teamB_pointA, teamB_pointB, teamB_pointC)#test printing
round_loop = 0
start_money = 0
while round_loop != many_round:
    print()
    if start_money == 1:
        teamA_budget = teamA_budget + round_money
        teamB_budget = teamB_budget + round_money
        
    print("""
------------------------------------------------------------------------------
                round """, round_loop, "/", many_round, 
"""\n------------------------------------------------------------------------------""")

    print("""
------------------------------------------------------------------------------
                team A is now choosing 
------------------------------------------------------------------------------""")

    
    print("\n")
    print("-----------------------------------------------------------------------")
    print("                 TEAM A POINT A")
    print("you have ${}".format(teamA_budget))
    troop_choose("teamA", "A")
    print("you have ${} left".format(teamA_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointA[0], teamA_pointA[1], teamA_pointA[2], teamA_pointA[3], teamA_pointA[4]))
    print("-----------------------------------------------------------------------")
    print("\n")



    print("-----------------------------------------------------------------------")
    print("                 TEAM A POINT B")
    print("you have ${}".format(teamA_budget))
    troop_choose("teamA", "B")
    print("you have ${} left".format(teamA_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointB[0], teamA_pointB[1], teamA_pointB[2], teamA_pointB[3], teamA_pointB[4]))
    print("-----------------------------------------------------------------------")
    print("\n")



    print("-----------------------------------------------------------------------")
    print("                 TEAM A POINT C")
    print("you have ${}".format(teamA_budget))
    troop_choose("teamA", "C")
    print("you have ${} left".format(teamA_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamA_pointC[0], teamA_pointC[1], teamA_pointC[2], teamA_pointC[3], teamA_pointC[4]))
    print("-----------------------------------------------------------------------")
    print("\n")
    clear()
    print("""
------------------------------------------------------------------------------
                team B is now choosing 
------------------------------------------------------------------------------""")
    

    print("-----------------------------------------------------------------------")
    print("                 TEAM B POINT A")
    print("you have ${} ".format(teamB_budget))
    troop_choose("teamB", "A")
    print("you have ${} left".format(teamB_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointA[0], teamB_pointA[1], teamB_pointA[2], teamB_pointA[3], teamB_pointA[4]))
    print("-----------------------------------------------------------------------")
    print("\n")
    

    print("-----------------------------------------------------------------------")
    print("                 TEAM B POINT B")
    print("you have ${}".format(teamB_budget))
    troop_choose("teamB", "B")
    print("you have ${} left".format(teamB_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointB[0], teamB_pointB[1], teamB_pointB[2], teamB_pointB[3], teamB_pointB[4]))
    print("-----------------------------------------------------------------------")
    print("\n")
    


    print("-----------------------------------------------------------------------")
    print("                 TEAM B POINT C")
    print("you have ${}".format(teamB_budget))
    troop_choose("teamB", "C")
    print("you have ${} left".format(teamB_budget))
    print("you have  {} rileman {} gunner {} sniper {} medic and {} tank".format(teamB_pointC[0], teamB_pointC[1], teamB_pointC[2], teamB_pointC[3], teamB_pointC[4]))
    print("-----------------------------------------------------------------------")
    print("\n")



    battle("A")
    battle("B")
    battle("C")
    round_loop = round_loop + 1
    start_money = 1
#riund wont work
print("""
------------------------------------------------------------------------------
                team A won {} rounds! 
------------------------------------------------------------------------------""".format(teamA_wins))
print("""
------------------------------------------------------------------------------
                team B won {} rounds! 
------------------------------------------------------------------------------""".format(teamB_wins))


    