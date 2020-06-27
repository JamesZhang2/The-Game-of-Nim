# Written by James Ruogu Zhang on June 15, 2020
# This program attemps to solve the Game of Nim.
# Each player takes turns to take stones from three piles of stones.
# They can take any number of stones from any pile, but they can't take nothing or take stones from multiple piles.
# The player who takes the last stone wins.
# If a player is in a losing position and it is his turn to move, he loses or must move into a winning position.
# If a player is in a winning position and it is his turn to move, he can move into a losing position.
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

pile1 = int(input("Enter number of stones in the first pile: "))
pile2 = int(input("Enter number of stones in the second pile: "))
pile3 = int(input("Enter number of stones in the third pile: "))
if isWinningPos[pile1][pile2][pile3] == True:
    print(pile1, pile2, pile3, "is a winning position.")
    print("Winning strategy:", strategy[pile1][pile2][pile3])
else:
    print(pile1, pile2, pile3, "is a losing position.")