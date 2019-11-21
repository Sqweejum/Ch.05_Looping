'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
done = False
wins = 0
losses = 0
while not done:

    #variables

    import random
    num=random.randint(1,3)
    x = int(input("1 = rock   2 = paper  3 = scissors    4 = quit  enter a number."))
    if num==1:
        print("rock")
        if x == 1:
            print("Tie game")
        elif x== 2:
            print("you win")
            wins+=1
        elif x==3:
            print("you lose")
            losses+=1
        else:
            done = True
    elif num==2:
        print("paper")
        if x==1:
            print("you lose")
            losses+=1
        elif x==2:
            print("tie game")
        elif x==3:
            print("you win")
            wins+=1
        else:
            done = True

    else:
        print("scissors")
        if x==1:
            print("you win")
            wins+=1
        elif x==2:
            print("you lose")
            losses+=1
        elif x==3:
            print("tie game")
        else:
            done =True

print("wins:", wins, "   losses:", losses)



















