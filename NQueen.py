import array as arr
size = 8 #size of the board
lNum = [[ None for y in range(size)] for x in range(size)] #the 2d array
state = True
def setUp (): # set all the elements in the array to 0
    for i in range (size):
        for j in range (size):
            lNum[i][j] = 0
def printAll () : # print the board
    for i in range (size):
        tempString = ""
        for j in range (size):
            tempString += str(lNum[i][j])
            if (j == size-1):
                print (tempString)
def check(row, col): # checking if the queen is touching any other queens
    for i in range (size):
        if (lNum[row][i] == 1):
            return False
        if (lNum[i][col] == 1):
            return False
        for j in range (size):
            if ((i+j) == (row+col)):
                if (lNum[i][j] == 1):
                    return False
            if ((i-j) == (row-col)):
                if (lNum[i][j] == 1):
                    return False
    if (i == size-1): 
        return True
def solve(row, col, Q): # solving the n queen problem
    tempb = False
    while (tempb == False):
        if (check(row, col) == True):
            if (row < size):
                lNum[row][col] = 1
                if (Q < size-1):
                    Q = Q + 1
                    tempb = solve(row, col, Q)
                    if (tempb == False): 
                        Q = Q - 1
                        lNum[row][col] = 0
                elif (Q == size-1):
                    return True
        col = col + 1
        if (col == size):
            row = row + 1
            col = 0
            if (row == size):
                tempb = True
                return False
setUp()
solve( 0, 0, 0)
printAll()