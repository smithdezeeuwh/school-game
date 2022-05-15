import time

def delay_print(s):
    for char in s:
        print(char, end='')
        time.sleep(0.0007)
    print(" \n")

def start_input_def(start_input_raw_def):
    start_input_def = start_input_raw_def.lower()
    if start_input_def == "f":
        fight()
    elif start_input_def == "s":
        settings()
    elif start_input_def == "h":
        helpme()
    elif start_input_def == "hugoissupercool":
        cheatcodes()

def fight():
    global startloop
    startloop = False
    delay_print("fight")
    delay_print("choose your level")
    print("""
----------------------------------------------------------------------
I    level 1     I    level 2    I       level 3     I    level 4    I
I Dense canadian I barren afghan I  detroyed russian I  german power I
I    forest      I    desert     I       city        I     plant     I
I                I               I                   I               I
I  difficulty    I difficulty    I    difficulty     I difficulty    I
I    easy        I   mediun      I      mediumm      I     hard      I
I    {}    I  {}     I     {}      I   {}    I
----------------------------------------------------------------------

""".format(lvl1lock, lvl2lock, lvl3lock, lvl4lock))
    
    fight_loop = True
    
    while fight_loop:
        delay_print("what level would you like to fight in")
        start_fight = input()
    
        if start_fight == "1" or start_fight == "level 1":
            if lvl1lock == "unlocked":
                delay_print("level 1 fight")
                fight_loop = False
            elif lvl1lock == "  locked":
                delay_print("level 1 is locked")
            else:
                delay_print("error at level 1 lock")
        elif start_fight == "2" or start_fight == "level 2":
            if lvl2lock == "unlocked":
                delay_print("level 2 fight")
                fight_loop = False
            elif lvl2lock == "  locked":
                delay_print("level 2 is locked")
            else:
                delay_print("error at level 2 lock")
        elif start_fight == "3" or start_fight == "level 3":
            if lvl3lock == "unlocked":
                delay_print("level 3 fight")
                fight_loop = False
            elif lvl3lock == "  locked":
                delay_print("level 3 is locked")
            else:
                delay_print("error at level 3 lock")
        elif start_fight == "4" or start_fight == "level 4":
            if lvl4lock == "unlocked":
                delay_print("level 4 fight")
                fight_loop = False
            elif lvl4lock == "  locked":
                delay_print("level 4 is locked")
            else:
                delay_print("error at level 4 lock")
        else:
            delay_print("sorry please enter a level you would like to play in")
            delay_print("try (1) or (level 1)")

def settings():
    delay_print("settings")

def helpme():
    delay_print("helpme")
def cheatcodes():
    delay_print("hugoissupercool")

lvl1lock = "unlocked"
lvl2lock = "  locked"
lvl3lock = "  locked"
lvl4lock = "  locked"






startloop = True
while startloop:
    delay_print("welcome to Battle land 2043")
    delay_print("in this game you will fight in places all across the world")
    delay_print("enter f to fight ")
    delay_print("enter s for setting")
    delay_print("enter h for how to play")
    start_input_raw = input()
    start_input_def(start_input_raw)



