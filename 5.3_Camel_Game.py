'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random
num = random.randint(6,12)
num2 = random.randint(10,20)

#variables
water = 4
camel = 0
bandit = -20
distance = 0
thirst = 0


v = input("welcome to the camel game would you like instructions?"
          "   a. yes      b. no")
if v == ("a"):
    print("The goal of this game is to make it 200 miles across the desert while bandits chase you."
          "during this time you need to make sure your camel is well rested and you have enough"
          "water to drink.")
else:
    print("ah I see a fellow desert dweller.")

done = False
while not done:
    z = input("what will you do?"
              "   a.Drink from your canteen"
              "   b.Ahead moderate speed"
              "   c.Ahead full speed"
              "   d. stop for the night"
              "   e. status check"
              "   q.Quit")
    if z == ("q"):
        done = True
    elif z == ("a"):
        thirst = 0
        water -= 3



