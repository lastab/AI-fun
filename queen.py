

SIZE = 8
board =[[0 for x in range(SIZE)] for y in range(SIZE)]

def moveQueen(row):
    if 1 in board[row]:
        j = board[row].index(1)
        board[row][j] = 0
        j += 1
        if j ==SIZE:
            return False
        else:
            board[row][j] = 1
            return True
    else:
        j = findSpaceAt(row)
        if j != -1:
            board[row][j] = 1
            return True
        else:
            return False


def findSpaceAt(row):
    possible_space = -1
    j = 0
    while j < SIZE:
        vertical = searchAt(row,j,0)
        p45 = searchAt(row,j,1)
        m45 = searchAt(row,j,-1)
        if vertical and p45 and m45:
            possible_space = j
            break

        j += 1

    return possible_space


def searchAt(row, col, change):
    possible = True
    row -= 1
    col += change
    while row>= 0 and col>=0 and col<SIZE:
        if board[row][col] == 1:
            possible = False
            break

        row -= 1
        col += change


    return possible


def printBoard(board):
    i = 0
    while i < SIZE:
        row = ""
        j = 0
        while j < SIZE:
            if board[i][j] == 1:
                row += 'Q'
            else:
                row += 'o'

            j += 1

        print(row)
        i += 1



i = 0
while i < SIZE:
    if moveQueen(i):
        i += 1
    else:
        i -= 1
        if i < 0:
            break


printBoard(board)
print(board)
