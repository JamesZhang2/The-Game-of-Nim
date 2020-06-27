# Written by James Ruogu Zhang on June 15, 2020
# This program attemps to solve the Game of Nim.
# Each player take turns to take stones from three piles of stones.
# They can take any number of stones from any pile, but they can't take nothing or take stones from multiple piles.
# The player who takes the last stone wins.
# If a player is in a losing position and it is his turn to move, he loses or must move into a winning position.
# If a player is in a winning position and it is his turn to move, he can move into a losing position.
import random

isWinningPos = []
strategy = []
for i in range (11):
    isWinningPos.append([])
    strategy.append([])
    for j in range (11):
        isWinningPos[i].append([])
        strategy[i].append([])
        for k in range (11):
            isWinningPos[i][j].append(False)
            strategy[i][j].append(-1)

# Basic step
isWinningPos[0][0][0] = False
for i in range (11):
    isWinningPos[0][0][i] = True
    isWinningPos[0][i][0] = True
    isWinningPos[i][0][0] = True
    strategy[0][0][i] = [0, 0, 0]
    strategy[0][i][0] = [0, 0, 0]
    strategy[i][0][0] = [0, 0, 0]
    
    isWinningPos[0][i][i] = False
    isWinningPos[i][0][i] = False
    isWinningPos[i][i][0] = False

for i in range (1, 11):
    for j in range (1, i):  # Note that j is smaller than i
        isWinningPos[0][j][i] = True
        strategy[0][j][i] = [0, j, j]
        isWinningPos[0][i][j] = True
        strategy[0][i][j] = [0, j, j]
        isWinningPos[j][0][i] = True
        strategy[j][0][i] = [j, 0, j]
        isWinningPos[i][0][j] = True
        strategy[i][0][j] = [j, 0, j]
        isWinningPos[j][i][0] = True
        strategy[j][i][0] = [j, j, 0]
        isWinningPos[i][j][0] = True
        strategy[i][j][0] = [j, j, 0]

# Inductive step
for i in range (1, 11):
    for j in range (1, 11):
        for k in range (1, 11):
            # Check every possible position
            # First keep j and k constant
            for x in range (0, i):
                if isWinningPos[x][j][k] == False:
                    isWinningPos[i][j][k] = True
                    strategy[i][j][k] = [x, j, k]
            # Next keep i and k constant
            for y in range (0, j):
                if isWinningPos[i][y][k] == False:
                    isWinningPos[i][j][k] = True
                    strategy[i][j][k] = [i, y, k]
            # Finally keep i and j constant
            for z in range (0, k):
                if isWinningPos[i][j][z] == False:
                    isWinningPos[i][j][k] = True
                    strategy[i][j][k] = [i, j, z]

def printRules():
    print("Welcome to the Game of Nim!")
    print("Each player takes turns to take stones from three piles of stones.")
    print("They can take any number of stones from any pile, but they can't take nothing or take stones from multiple piles.")
    print("The player who takes the last stone wins.")
    print("You will play against the computer.")

printRules()
pile1 = random.randint(1, 10)
pile2 = random.randint(1, 10)
pile3 = random.randint(1, 10)
print("The three piles of stones are:", pile1, pile2, pile3)
isHumanTurn = input("Do you want to play first? (Y/N) ")
while isHumanTurn != "Y" and isHumanTurn != "N":
    isHumanTurn = input("Do you want to play first? (Y/N) ")

while pile1 != 0 or pile2 != 0 or pile3 != 0:
    if isHumanTurn == "N":  # Computer's turn
        print("Computer's turn!")
        if isWinningPos[pile1][pile2][pile3] == True:  # The computer is at a winning position.
            pile1_temp = strategy[pile1][pile2][pile3][0]
            pile2_temp = strategy[pile1][pile2][pile3][1]
            pile3_temp = strategy[pile1][pile2][pile3][2]
            pile1 = pile1_temp
            pile2 = pile2_temp
            pile3 = pile3_temp
        else:  # The computer is at a losing position
            if pile1 != 0:
                pile1 -= 1
            elif pile2 != 0:
                pile2 -= 1
            else:
                pile3 -= 1
        print("The three piles of stones are now:", pile1, pile2, pile3)
        isHumanTurn = "Y"
    else:  # Human's turn
        print("Your turn!")
        pileNumber = int(input("Which pile do you want to take stones from? "))
        stones = int(input("How many stones do you want to take from this pile? "))
        if pileNumber == 1:
            pile1 -= stones
        elif pileNumber == 2:
            pile2 -= stones
        else:
            pile3 -= stones
        print("The three piles of stones are now:", pile1, pile2, pile3)
        isHumanTurn = "N"

if isHumanTurn == "Y":  # Computer just took the last stone, human loses
    print("You lose!")
else:
    print("You win!")