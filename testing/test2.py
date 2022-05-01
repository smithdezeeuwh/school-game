

def troop_half(team_half):
    for i in range(0,5):
        if type(int(team_half[i]*0.5)) == float:
            print("that is a dec",team_half[i])
            team_half[i] = team_half[i] - 1
            team_half[i] = team_half[i]*0.5
        else:
            print("that is  not a dec",team_half[i])
            
            team_half[i] = team_half[i]*0.5
    return team_half

z = [0,1,2,3,4,5]
print(troop_half(z))
