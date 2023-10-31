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
    for y in range(0,sides):
        if(rolled[y] != 0):
            print("Number of "+ str(y + 1) + "'s Rolled:" , rolled[y])  
    print()
###################################################################
    #ERROR BLOCK
def error():
    print("Error, please input a valid input.")
###################################################################
    #Prompts the user if they would like to repeat the program
def contTest():
    print()
    contPrompt = input("Would you like to roll another set? (Y/N) :")
    if contPrompt == "N" or contPrompt == 'n':
        return False
    elif contPrompt == "Y" or contPrompt == "y":
        return True
    else:
        error()
###################################################################
cont = True
while cont:
    print()
    sidesPrompt = int(input("How many sides does the dice have?: "))
    numOfRolls = int(input("How many times would you like to throw the dice?: "))
    #Creating an Array with the size of the sides
    numberRolled = [0] * sidesPrompt

    if numOfRolls > 0:
    
        #Loop the amount of times user designated
        i=0
        for i in range(0,numOfRolls):

            #Rolls a dice
            diceRoll = random.randint(0,sidesPrompt-1)
            #Increments the List in the index of the roll
            numberRolled[diceRoll] += 1
            
        #Print each number rolled as long as there is data stored
        diceStats(sidesPrompt, numberRolled)

        #Create a bar graph based on percentage
        buildBarGraph(sidesPrompt, numberRolled, numOfRolls)

    else:
        error()
        
    cont = contTest()
    
