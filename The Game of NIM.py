# Written by James Zhang on February 6, 2020
# This program will play the game of NIM with a player.
def PrintRules():
    print("Let's play a game of NIM.")
    print("Here are 4 piles of stone. Each pile has 0-100 stones.")
    print("We take these stones in turns.")
    print("The current player can take any number of stones from any pile.")
    print("However, the player can only take stones from one pile at a time.")
    print("The player who takes the last stone wins.")
    print("The computer will go first.")
    for i in range (1,5):
        temp = int(input("Enter number of stones in pile " + str(i) + ": "))
        while temp < 0 or temp > 100:
            print("The number of stones in each pile must be between 0 and 100.")
            temp = int(input("Enter number of stones in pile " + str(i) + ": "))
        stone.append(temp)

def TotalStones():
    allStones = 0  # Reset allStones
    for i in range (0,4):
        allStones += stone[i]
    return allStones

def ConvertBase():
    base = 2
    for i in range (0,4):
        num = stone[i]
        digit[i] = [0,0,0,0,0,0,0]  # Reset digit
        # Short Division
        currentDigit = 0
        while num != 0:
            digit[i][currentDigit] = num % base
            num = num // base
            currentDigit += 1

def CheckBalance():
    IsBalanced = True
    ConvertBase()
    digitSum = [0,0,0,0,0,0,0]  # Reset digitSum
    for i in range (0,7):
        for j in range (0,4):
            digitSum[i] += digit[j][i]
        if digitSum[i] % 2 == 1:
            IsBalanced = False
    return IsBalanced

def FindMax():
    stoneMax = 0
    for i in range (1,4):
        if stone[i] > stone[stoneMax]:
            stoneMax = i
    return stoneMax
    
stone = []
digit = []
IsBalanced = True
allStones = 0
for i in range (0,4):
    digit.append([0,0,0,0,0,0,0])
digitSum = [0,0,0,0,0,0,0]

PrintRules()
allStones = TotalStones()
compTurn = True
while allStones != 0:
    if compTurn == True:
        # Computer's turn
        IsBalanced = CheckBalance()
        if IsBalanced == True:
            # Computer in P position, will lose if player doesn't make a mistake
            # Take a stone from the maximum pile
            stoneMax = FindMax()
            stone[stoneMax] -= 1
            print("Computer took 1 stone from pile " + str(stoneMax+1) + ".")
            print("Current situation: " + str(stone))
        else:
            # Computer in N position, will win
            for pile in range (0,4):
                stonesTaken = 0
                while IsBalanced == False and stone[pile] > 0:
                    # Keep taking stones until IsBalanced == True or the pile is empty
                    stone[pile] -= 1
                    stonesTaken += 1
                    IsBalanced = CheckBalance()
                if IsBalanced == False: # Still unbalanced, pile is empty
                    stone[pile] += stonesTaken
                    # Try another pile
                else:  # Balanced
                    print("Computer took " + str(stonesTaken) + " stone(s) from pile " + str(pile+1) + ".")
                    print("Current situation: " + str(stone))
                    break
        compTurn = False
    else:
        # Player's Turn
        pile = int(input("Which pile do you want to take stones from? ")) - 1
        while pile < 0 or pile > 4:
            print("There are only 4 piles of stones.")
            pile = int(input("Which pile do you want to take stones from? ")) - 1
        while stone[pile] == 0:
            print("There are no more stones in this pile.")
            pile = int(input("Which pile do you want to take stones from? ")) - 1
        stonesTaken = int(input("How many stones do you want to take from this pile? "))
        while stonesTaken < 1 or stonesTaken > stone[pile]:
            print("Please take a valid number of stones from this pile.")
            stonesTaken = int(input("How many stones do you want to take from this pile? "))
        stone[pile] -= stonesTaken
        print("You took " + str(stonesTaken) + " stone(s) from pile " + str(pile+1) + ".")
        print("Current situation: " + str(stone))
        compTurn = True

    allStones = TotalStones()  # Update allStones

if compTurn == True:
    print("You win!")
else:
    print("Computer wins!")
