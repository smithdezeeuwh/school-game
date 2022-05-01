teamA = [0, 0]
teamB = [0, 0]
def battle(teamA_battle, teamB_battle)
    global live_battle 
    
    teamA_battlepower = teamA_battle[0]*1 + teamA_battle[1]*2 + teamA_battle[2]*3 + teamA_battle[3]*4 + teamA_battle[4]*7
    teamB_battlepower = teamB_battle[0]*1 + teamB_battle[1]*2 + teamB_battle[2]*3 + teamB_battle[3]*4 + teamB_battle[4]*7
    if teamA_battlepower > teamB_battlepower:
        battle_dif = teamA_battlepower - teamB_battlepower
        battle_win = "team A"
        battle_lose = "team B"
    else:
        battle_dif = teamB_battlepower - teamA_battlepower
        battle_win = "team B"
        battle_lose = "team A"
    print("----------------------{} WON!---------------------".format(battle_win))
    if battle dif > 50:
        print("{} destroyed {} by {} points".format(battle_win, battle_lose, battle_dif)
    elif battle dif > 10:
        print("{} won by {} points".format(battle_win, battle_dif)
    elif battle dif == 0:
        print("TIE")
