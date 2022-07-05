import random
import time
#constants
SOLDIER_COST = 1
GUNNER_COST = 2
SNIPER_COST = 2.5
MEDIC_COST = 3
ENGINEER_COST = 4
TANK_COST = 6


#####this here is the main battle system
def global_level(level):
    #these change values of troops depending on level selection
    if level == "canada":
        soldier_power = 3
        gunner_power = 4
        sniper_power = 3 
        medic_power = 3 
        engineer_power = 3
        tank_power = 4
        soldier_gunner_buff = 0.6
        sniper_medic_buff = 0.4 
        engineer_tank_buff = 0.2
        enemy_money_added = 50
        user_money_added = 50
        print("\nwelcome to the deep forests of canada.")
        print("infantry units are especially effective in the forest.")
        print("tanks are not. They struggle amougst the trees\n")
        etgp1 = [1,1,1,1,1,1]
        etgp2 = [50,20,20,20,20,20]

    elif level == "afganistan":
        soldier_power = 1
        gunner_power = 2
        sniper_power = 3
        medic_power = 3
        engineer_power = 5
        tank_power = 9
        soldier_gunner_buff = 0.1
        sniper_medic_buff = 0.5
        engineer_tank_buff = 0.4
        enemy_money_added = 70
        user_money_added = 50
        print("\nwelcome to the barren deserts of afganistan.")
        print("sniper units are especially effective in the desert.")
        print("Ground units are more exposed in the desert\n")
        etgp1 = [3,3,1,1,0,0]
        etgp2 = [20,20,20,20,20,20]

    elif level == "russia":
        soldier_power = 2 
        gunner_power = 3
        sniper_power = 5
        medic_power = 4 
        engineer_power = 3
        tank_power = 2 
        soldier_gunner_buff = 0.4
        sniper_medic_buff = 0.6
        engineer_tank_buff = 0
        enemy_money_added = 100
        print("\nwelcome to the destroyed city of volgograd, Russia.")
        print("sniper and other ground units are especially effective in urban areas.")
        print("Tanks are highly vulnerable in urban combat\n")
        etgp1 = [1,1,5,5,0,0]
        etgp2 = [50,20,20,20,7,7]
        user_money_added = 50

        
    elif level == "germany":
        print("\nwelcome to Bernhard power plant, Germany.")
        print("enemys have been stationed here since the 1940s   \n that means that they know the area like the back of there hand")
        print("buff are decreased due to conditiions")
        soldier_power = 1
        gunner_power = 3
        sniper_power = 3
        medic_power = 4
        engineer_power = 4
        tank_power = 6
        soldier_gunner_buff = 0.1
        sniper_medic_buff = 0.2
        engineer_tank_buff = 0.3
        enemy_money_added = 100
        etgp1 = [0,0,3,3,0,0]
        etgp2 = [10,10,30,30,4,4]
        user_money_added = 75
        
    else:
        print("error at top of global level")
    ######this def here checks the input to make sure it is 0 0 0 0 0 0  characters and not 0 0 0 0 0 or something else
    def troop_input():
        error = "\n error: you have enter an incorrect input"
        loop = 1
        while loop == 1: 
            main = input("input:")
            try:
                main1 = main.split()
                for i in range(len(main1)):
                    main1[i] = int(main1[i])
                if len(main1) == 6:
                    loop = 2
                    return main1
                else:
                    print(error)
            except:
                print(error)

    ######this varible checks how many times troops can buff like 5 soldiers and 8 gunners can buff 5 times
    def difference(num1, num2):
        points = 0
        loop = 1
        while loop == 1:
            points += 1
            num1 -= 1
            num2 -= 1
            
            if num1 or num2 == 0:
                loop = 2
                return points
    #this def checks for buffs ex: 1 2 0 0 0 0 will add soldier gunner buff
    def buff_check(user_troops):
        multiplyer = 1
        ##this is for some dumb error
        user_troops0 = user_troops[0]
        user_troops1 = user_troops[1]
        user_troops2 = user_troops[2]
        user_troops3 = user_troops[3]
        user_troops4 = user_troops[4]
        user_troops5 = user_troops[5]
        

        #EACH POWER ADDS TO A TOTAL POWER MULTIPLYER
        #this are the checks for buffs
        if user_troops0 and user_troops1 != 0:
            print("infantry and gunner buff time")
            infantry_buff = difference(user_troops[0], user_troops[1])
            infantry_buff = infantry_buff * soldier_gunner_buff
            multiplyer += infantry_buff
                                    
        if user_troops2 and user_troops3 != 0:
            print("sniper and gunner buff time")
            infantry_buff = difference(user_troops[2], user_troops[3])
            infantry_buff = infantry_buff * sniper_medic_buff
            multiplyer += infantry_buff
        if user_troops4 and user_troops5 != 0:
            print("tank and engineer buff time")
            
            infantry_buff = difference(user_troops[4], user_troops[5])
            infantry_buff = infantry_buff * engineer_tank_buff
            multiplyer += infantry_buff
        if multiplyer == 1:
            print("no buff")
        #this line of codes adds all the troops powers 
        power1 = user_troops[0]*soldier_power + user_troops[1]*gunner_power + user_troops[2]*sniper_power + user_troops[3]*medic_power + user_troops[4]*engineer_power + user_troops[5]*tank_power 
        #then this multiplys it with the buffs
        power = power1 * multiplyer
        print(power)
        return power
        #as the name says this def generates enemy troops 
    def enemy_troop_generation():
        global enemy_balance 
        enemy_multiplier = 0
        enemy_troops = [0,0,0,0,0,0]
        loop =  1
        print("\n generating enemy troops\n (this may take a bit)")
        while loop == 1:

             #this is what generates the enemy troops 
            enemy_troops[0] = random.randint(etgp1[0],etgp2[0])
            enemy_troops[1] = random.randint(etgp1[1],etgp2[1])
            enemy_troops[2] = random.randint(etgp1[2],etgp2[2])
            enemy_troops[3] = random.randint(etgp1[3],etgp2[3])
            enemy_troops[4] = random.randint(etgp1[4],etgp2[4])
            enemy_troops[5] = random.randint(etgp1[5],etgp2[5])
            enemy_troops_cost = enemy_troops[0]*soldier_power + enemy_troops[1]*gunner_power + enemy_troops[2]*sniper_power + enemy_troops[3]*medic_power + enemy_troops[4]*engineer_power + enemy_troops[5]*tank_power
            #this checks if the enemy has enough money and then returns it
            if enemy_troops_cost < enemy_balance:
                if level == "germany":
                    enemy_troops = enemy_troops * 2
                print("the enemy troops that were generated {}".format(enemy_troops))
                print("\n Done \n")
                loop = 2
                enemy_balance = enemy_balance - enemy_troops_cost
                print("enemy spent cost ", enemy_troops_cost)
                return enemy_troops
    #this def checks the users balance to make sure they have enough money
    def cost_loop():
        global lvl1lock 
        global lvl2lock 
        global lvl3lock
        global lvl4lock
        
        global user_balance
        loop = 1
        while loop == 1:
            user_troops = troop_input()

            
            user_troops_cost = user_troops[0]*1 + user_troops[1]*2 + user_troops[2]*2.5 + user_troops[3]*3 + user_troops[4]*4 + user_troops[5]*6 
            difference =  user_balance - user_troops_cost 
            if difference >= -1 :
                rusure = input("Are you sure? it costs ${} (press enter to confirm)".format(user_troops_cost))
                if  rusure == "":
                    loop = 2
                    user_balance -= user_troops_cost
                    print("that cost ", user_troops_cost)
                    user_power = buff_check(user_troops)
                    return user_power
                #this is just for testing
                elif  rusure == "testcode":
                    loop = 2
                    user_power = 10000000
                    lvl1lock = "unlocked"
                    lvl2lock = "unlocked"
                    lvl3lock = "unlocked"
                    lvl4lock = "unlocked"
                    return user_power
            else:
                print("sorry you dont have enough money")
                missing =  user_troops_cost - user_balance 
                print("you are missing $", missing)
                
    def troop_costs():
        #just a simple cost and instructions print 
        print('''
\n
these are the costs and power of different troops
soldier is $1 and {} power
gunner is $2 and {} power
sniper is $2.5 and {} power
medic is $3 and {} power
engineer is $4 and {} power
tank is $6 and {} power
rilfman and gunner add {} buff to power
sniper and medic add {} buff to power
engineer and tank add {} buff to power
\n


        \n
        '''.format(soldier_power,gunner_power,sniper_power,medic_power,engineer_power,tank_power,soldier_gunner_buff,sniper_medic_buff,engineer_tank_buff))
                

    troop_types = ["soldier,gunner,sniper,medic,engineer,tank"]
    #main user troop inpit system
    #medic buff sniper
    #gunners buff sniper
    #engineer buff tank
    user_balance = 0
    enemy_balance = 0
    enemy_balance = 1000





#this def is the loop that runs the whole battle eg:compares powers and determins who is winning  
    def battle_loop():
        global global_lock
        global user_balance
        global enemy_balance
        
        user_balance = 0
        enemy_balance = 0
        enemy_health = 1000
        user_health = 1000
        troop_costs()
        print("let the battle start")
        loop = 1
        battle_round = 1
        while loop == 1:
            print("""
\n
\n
    ------------------------------------------------------------------------------
                                ROUND {}
    ------------------------------------------------------------------------------
    costs:
          soldier  gunner  sniper  medic  engineer  tank
    costs   1      2        2.5      3      4        6
    power   {}      {}         {}       {}      {}        {}
    \n
    \n
    """.format(battle_round,soldier_power,gunner_power,sniper_power,medic_power,engineer_power,tank_power))
            if battle_round != 1:
                if user_health > enemy_health:
                    print("you are winning")
                else:
                    print("you are losing")
            user_balance = user_balance + user_money_added
            enemy_balance = enemy_balance + enemy_money_added 
            print("you have {} money and {} health".format(user_balance, user_health))
            print("the enemy has {} money and {} health".format(enemy_balance, enemy_health))
            user_power = cost_loop()
            enemy_power = buff_check(enemy_troop_generation())########average about 280 power
            print("user power:{}    enemy power:{}".format(user_power,enemy_power))
            enemy_health = enemy_health - user_power
            user_health = user_health - enemy_power
            #when someone wins this returns sets gobal lock to unlocked then unlocks the next level 
            if enemy_health < 0:
                print("you win")
                loop = 2
                print("you have {} money and {} health".format(user_balance, user_health))
                print("the enemy has {} money and {} health".format(enemy_balance, enemy_health))
                global_lock = "unlocked"
            elif user_health < 0:
                print("you lose :( ")
                loop = 2
                print("you have {} money and {} health".format(user_balance, user_health))
                print("the enemy has {} money and {} health".format(enemy_balance, enemy_health))
                global_lock = "  locked"
            battle_round += 1
            
    
    

            
            
                  
    battle_loop()



#this checks the menu input
def start_input_def(start_input_raw_def):
    start_input_def = start_input_raw_def.lower()
    if start_input_def == "f":
        level_select()
    elif start_input_def == "s":
        settings()
    elif start_input_def == "h":
        helpme()
    elif start_input_def == "hugoissupercool":
        cheatcodes()
#this here is level selection
def level_select():
    global global_lock
    global lvl1lock
    global lvl2lock
    global lvl3lock
    global lvl4lock
    global startloop
    startloop = False
    print("fight")

    
    fight_loop = True
    
    while fight_loop:
        print("\n \nchoose your level")
        print("""
----------------------------------------------------------------------
I    level 1     I    level 2    I       level 3     I    level 4    I
I Dense canadian I barren afghan I  detroyed russian I  german power I
I    forest      I    desert     I       city        I     plant     I
I                I               I                   I               I
I  difficulty    I difficulty    I    difficulty     I difficulty    I
I    easy        I   medium      I       hard        I     extreme   I
I    {}    I  {}     I     {}      I   {}    I
----------------------------------------------------------------------
\n
\n


""".format(lvl1lock, lvl2lock, lvl3lock, lvl4lock))
        print("what level would you like to fight in")
        start_fight = input()
    
        if start_fight == "1" or start_fight == "level 1":
            if lvl1lock == "unlocked":
                print("level 1 fight")
                global_level("canada")
                lvl2lock = global_lock

                
            elif lvl1lock == "  locked":
                print("level 1 is locked")
            else:
                print("error at level 1 lock")
        elif start_fight == "2" or start_fight == "level 2":
            if lvl2lock == "unlocked":
                print("level 2 fight")
                global_level("afganistan")
                lvl3lock = global_lock
                
                
                
            elif lvl2lock == "  locked":
                print("level 2 is locked")
            else:
                print("error at level 2 lock")
        elif start_fight == "3" or start_fight == "level 3":
            if lvl3lock == "unlocked":
                print("level 3 fight")
                global_level("russia")
                lvl4lock = global_lock

                


                
            elif lvl3lock == "  locked":
                print("level 3 is locked")
            else:
                print("error at level 3 lock")
        elif start_fight == "4" or start_fight == "level 4":
            if lvl4lock == "unlocked":
                print("level 4 fight")
                global_level("germany")
                if global_lock == "unlocked":
                     fight_loop = False
                     print("congratulations on finishing my game. thank you for playing")
                

                
            elif lvl4lock == "  locked":
                print("level 4 is locked")
            else:
                print("error at level 4 lock")
        else:
            print("sorry please enter a level you would like to play in")
            print("try (1) or (level 1)")
#these arent done
def settings():
    print("settings")

def helpme():
    print("how to play")
    print("""READ THE WHOLE THING PLEASE:
please format your input like this:
 x(rifleman) x(gunner)x (sniper) x(medic) x(tank)
so if you wanted 1 rifleman 2gunner 1sniper 2 medic 1 engineer 1 tank
it would go like this: 1 2 1 2 1 1")
or if you wanted 1 soldier it would look like this:1 0 0 0 0 0
\n
check buffs! they help ALOT\n
when have 1 1 0 0 0 0 it will add 0.2 to a multiplyer (0.2 depending on the level)
\n if you had 2 2 0 0 0 0 it will add 0.4 to a multiplyer \n
everytime you have a pair of 2 troops( either soldier + gunner or sniper+medic or engineer+tank)\n
it adds to a global multipyer. this multiply will be timeds with your troops power to make your final power.\n
example 1 1 0 0 1 1\n
trooppower = 1 + 2 + 3 + 5 = 11(values change depending on level)\n
multiplyer = 1(base multiplyer) + 0.2 + 0.6 = 1.8\n
final power = 11 x 1.8 = 19.8
\n
\n""")
def cheatcodes():
    print("hugoissupercool")

#these variable lock or lock levels 
lvl1lock = "unlocked"
lvl2lock = "  locked"
lvl3lock = "  locked"
lvl4lock = "  locked"
#### etgp stand for enemy troop generation paraaters
etgp1 = [0,0,0,0,0,0]
etgp2 = [0,0,0,0,0,0]





#this is the start of my game
startloop = True
while startloop:
    print("welcome to Battle land 2043")
    
    print("in this game you will fight in places all across the world")
    print("enter f to fight ")
    print("enter s for setting")
    print("enter h for how to play")
    start_input_raw = input()
    start_input_def(start_input_raw)
