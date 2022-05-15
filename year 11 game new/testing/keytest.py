def clear():
    x = 0
    while x != 10:
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        x = x + 1






loop = True
inv = ["sword","bottle","book"]
while loop:
    
    print("this is ur inv")
    print(inv)
    drop = int(input("what item would u like to drop"))
    drop = drop - 1
    print("u dropped",inv[drop])
    del inv[drop]
    poop = input("clear?")
    if poop == "clear":
        clear()

