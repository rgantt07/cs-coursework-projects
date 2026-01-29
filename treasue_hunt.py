import random

width = int(input("Enter the width of the grid: "))
height = int(input("Enter the height of the grid: "))
board = []
numberOfUndiscoveredTreasures = 0
for i in range(height):
    row = []
    board.append(row)
    for j in range(width):
        num = random.random()
        if num >= 0.7:
            numberOfUndiscoveredTreasures += 1
            cell = "T"
            row.append(cell)
        else:
            cell = "O"
            row.append(cell)

print("Number of treasures hidden:", numberOfUndiscoveredTreasures)

while numberOfUndiscoveredTreasures != 0:
    row = int(input(f'Enter the row number (0 to {width - 1}): '))
    column = int(input(f'Enter the column number (0 to {height - 1}): '))
    if board[row][column] == "T":
        cell = board[row][column]
        board[row][column] = "X"
        numberOfUndiscoveredTreasures -= 1
        print("Congratulations! You found a treasure!", end="")
        for i in range(width):
            print("")
            for j in range(height):
                if board[i][j] == "T":
                    print("O", end=" ")
                else:
                    print(board[i][j], end=" ")
        print("")
    else:
        print("No treasure here, try again!")

    if numberOfUndiscoveredTreasures == 0:
        print("Congratulations! You found all the treasure!", end="")
        for i in range(width):
            print("")
            for j in range(height):
                print(board[i][j], end=" ")
        break








