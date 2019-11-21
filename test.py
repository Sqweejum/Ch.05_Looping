done = False
while not done:

    import random
    num = random.randint(1,3)
#variables
    wins = 0
    losses = 0



    x = int(input("1 = rock   2 = paper  3 = scissors    4 = quit  enter a number."))
    if num == 1:
        print("rock")
        if x == 1:
            print("Tie game")
        elif x == 2:
            print("you win")
            wins+=1
        else:
            print("you lose")
            losses+=1
    elif num == 2:
        print("paper")
        if x == 1:
            print("you lose")
            losses+=1
        elif x == 2:
            print("tie game")
        elif x == 3:
            print("you win")
            wins+=1
    elif num == 3:
        print("scissors")
        if x == 1:
            print("you win")
            wins+=1
        elif x == 2:
            print("you lose")
            losses+=1
        else:
            print("tie game")
    else:
        if x ==4:
            done=True
