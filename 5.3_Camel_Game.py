'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random



#variables
water = 4
camel = 0
bandit = 0
distance = 15
thirst = 0


v = input("welcome to the camel game would you like instructions? "
          "   a. yes      b. no")
if v == ("a"):
    print("The goal of this game is to make it 200 miles across the desert while bandits chase you."
          "during this time you need to make sure your camel is well rested and you have enough"
          "water to drink if you water gets to 0 you lose and if you camel gets to 8 tiredness"
          "it will die.")
else:
    print("ah I see a fellow desert dweller.")

done = False
while not done:
    num = random.randint(6, 12)
    num2 = random.randint(10, 20)
    num3 = random.randint(2,4)
    num4 = random.randint(2,3)
    num5 = random.randint(1,20)
    z = input("what will you do?"
              "   a.Drink from your canteen"
              "   b.Ahead moderate speed"
              "   c.Ahead full speed"
              "   d. stop for the night"
              "   e. status check"
              "   q.Quit")
    if z.lower() == ("q"):
        done = True
    elif z.lower() == ("a"):
        thirst = 0
        water -=1
        print("you have",water,"drinks left")
    elif z.lower() ==("b"):
        distance+=num
        thirst+=1
        camel+=1
        bandit+=num
        print("you have traveled",distance, "miles")
        print("the bandits have traveled",bandit, "miles")
        if thirst >=4:
            print ("you are thirsty")
        if thirst >=6:
            print ("you died of thirst")
            done = True
        if camel >= 5:
            print("your camel is tired.")
        if camel >=8:
            print("your camel died of exhaustion.")
            done = True
        if num5 == 19:
            print("you have found an oasis!! you water bottle has been filled")
            water = 4
        if distance >= 200:
            print("You have made it across the desert and escaped the bandits!")
            done = True
        if bandit > distance:
            print("you have been caught by the bandits you lose")
            done = True
    elif z.lower() ==("c"):
        distance+= num2
        thirst+=1
        camel+=num3
        bandit+=num
        print("you have traveled",distance, "miles")
        print("the bandits have traveled",bandit, "miles")
        if thirst >=4:
            print ("you are thirsty")
        if thirst >=6:
            print ("you died of thirst")
            done = True
        if camel >= 5:
            print("your camel is tired.")
        if camel >=8:
            print("your camel died of exhaustion.")
            done = True
        if num5 == 19:
            print("you have found an oasis!! you water bottle has been filled")
            water = 4
        if distance >= 200:
            print("You have made it across the desert and escaped the bandits!")
            done = True
        if bandit > distance:
            print("you have been caught by the bandits you lose")
            done = True

    elif z.lower() ==("d"):
        camel=0
        bandit+=num
        thirst+=1
        print("you decided to stop for the night so your camel can rest")
    elif z.lower() ==("e"):
        print("water:",water)
        print("camel tiredness:",camel)
        print("thirst:",thirst)
        print("distance traveled:", distance,"miles")
        print("bandits traveled", bandit,"miles")