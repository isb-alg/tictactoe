## matrix is a 3x3 list
## States are: 0-System lost 1-User lost 2-Draw 3-Game in progress
def column(matrix, i):
    return [row[i] for row in matrix]

def diagonal(matrix):
    return [matrix[i][i] for i in range(3)]

def reverseDiagonal(matrix):
    return [matrix[i][2-i] for i in range(3)]

def drawgrid(matrix):
    for i in range(3): print(matrix[i])
    return
