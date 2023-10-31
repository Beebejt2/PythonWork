#Throws random dice a given number of times

import random
import math

###################################################################
#Create a bar graph based on percentage
def buildBarGraph(side, sideRolled, timesRolled):
    for row in range(0,side):
        percentRolled = (sideRolled[row] * 100 // timesRolled)
        print(("%3s")%(row + 1), "|", end ="")
        for col in range(0,percentRolled):
            print("*", end="")
        print()
###################################################################
#Print each number rolled as long as there is data stored
def diceStats(sides,rolled):
    for spot in range(0,sides):
        if(rolled[spot] != 0):
            print("Number of "+ str(spot + 1) + "'s Rolled:" , rolled[spot])  
    print()
###################################################################


cont = True

while cont:
    print()
    sidesPrompt = int(input("How many sides does the dice have?: "))
    numOfRolls = int(input("How many time would you like to throw the dice?: "))
    NumberRolled = [0] * sidesPrompt

    if numOfRolls > 0:
    
        i = 0
        
        #Loop the amount of times user designated

        while(i < numOfRolls):

            #Rolls a dice
            diceRoll = random.randint(1,sidesPrompt)
            NumberRolled[diceRoll-1] = NumberRolled[diceRoll - 1] + 1
            i = i + 1

        #Print each number rolled as long as there is data stored
        diceStats(sidesPrompt, NumberRolled)

        #Create a bar graph based on percentage
        buildBarGraph(sidesPrompt, NumberRolled, numOfRolls)

    else:
        print("Error, Please enter number larger than 0")
    print()

    contPrompt = input("Would you like to roll another set? (Y/N) :")
    if contPrompt == "N" or contPrompt == 'n':
        cont = False
    elif contPrompt == "Y" or contPrompt == "y":
        cont = True
