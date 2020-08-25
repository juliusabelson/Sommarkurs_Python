def transpose(matrix):
    if matrix == []:
        return []

    rows, columns = len(matrix), len(matrix[0])
    respVal = [[0 for x in range(rows)] for y in range(columns)]

    for i in range(columns):
        for j in range(rows):
            respVal[i][j] = matrix[j][i]

    return respVal

def powers(inputlist, start, stop):
    if inputlist == []:
        return []
    if stop < start:
        return [[]]

    rows, columns = len(inputlist), stop-start+1
    respVal = [[0 for x in range(columns)] for y in range(rows)]

    for i in range(rows):
        for j in range(columns):
            respVal[i][j] = inputlist[i]**(start+j)
    return respVal


def matmul(A, B):
    respVal = []
    if A == respVal or B == respVal:
        return respVal

    rows, columns = len(A), len(B[0]),
    respVal = [[0 for x in range(columns)] for y in range(rows)]

    for i in range(len(A)):  
        for j in range(len(B[0])):  
            for k in range(len(B)):  
                respVal[i][j] += A[i][k] * B[k][j] 

    return respVal

def invert(matrix):
    if matrix == []:
        return []

    rows, columns = len(matrix), len(matrix[0])
    respVal = [[0 for x in range(columns)] for y in range(rows)]
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    respVal[0][0] = matrix[1][1]/det
    respVal[1][0] = -matrix[1][0]/det
    respVal[0][1] = -matrix[0][1]/det
    respVal[1][1] = matrix[0][0]/det
    return respVal

def loadtxt(filepath):
    file = open(filepath, "r")
    respVal = [list(map(float, lines.strip().split("\t"))) for lines in file]

    return respVal
