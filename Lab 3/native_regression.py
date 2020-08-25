from matrix import *
import sys
import matplotlib.pyplot as plt

def main():
    #matrix = loadtxt(sys.argv[1])
    matrix = loadtxt("chirps.txt")
    
    X = [row[0] for row in matrix]
    Y = [row[1] for row in matrix]

    Xp  = powers(X, 0, 1)
    Yp  = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    Y2 = []
    for temperature in X:
        Y2.append(b + m * temperature)

    plt.plot(X,Y, 'ro')
    plt.plot(X,Y2)
    plt.show()



main()