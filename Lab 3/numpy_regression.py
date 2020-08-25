import sys
from matrix import loadtxt
import matplotlib.pyplot as plt
import numpy as np

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
    
    return np.array(respVal)

# Bad complexity but idc
def poly(a,x):
    respVal = []
    for temperature in x:
        tmpVal = 0
        for i in range(len(a)):
            tmpVal += a[i]*temperature**i
        
        respVal.append(tmpVal)

    return respVal
        

def main():
    matrix = loadtxt(sys.argv[1])
    n = int(sys.argv[2])
    #n = 2
    #matrix = loadtxt("chirps-modified.txt")
    
    X = [row[0] for row in matrix]
    Y = [row[1] for row in matrix]

    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = np.transpose(Xp)

    a = np.matmul(np.linalg.inv(np.matmul(Xpt,Xp)),np.matmul(Xpt,Yp))
    a = a[:,0]
    
    X2 = np.linspace(X[0],X[len(X)-1],500).tolist()
    Y2 = poly(a, X2)

    plt.plot(X,Y, 'ro')
    plt.plot(X2,Y2)
    plt.show()
    

main()