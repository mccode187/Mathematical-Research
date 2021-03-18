## Michael Chu
## 3/16/20

## Question: Given an n by n grid, how many vertical and horizontal lines do
## we need to ensure that there is an intersection ('incidence') in every
## diagonal?

## Equivalent arithmetic combinatorics question:
## Suppose S_1, S_2 are subsets of {0,1,2,...,n-1} and that
## {0,1,2,...,2(n-1)} is a subset of S_1 + S_2.
## How small could |S_1|+|S_2| be?

## Instruction to user: try running the program with different values of n!
## NOTE: This program implements the geometric interpretation of the problem.
## NOTE: This program MAY NOT NECESSARILY FIND THE OPTIMAL SOLUTION!!!
##          (I believe it only generates optimal solution up to n=7)
##       It only does an EDUCATED GUESS based on an algorithm.

# Checks if there is an incidence in every diagonal of matrix M
def incidenceInEveryDiagonal(M):
    for d in range(2*len(M)-1):
        incidence = False
        if d-(len(M)-1)>0:
            i = d-(len(M)-1) 
        else:
            i=0
        smallestPossible_i = i
        while not incidence and (d-i>=smallestPossible_i):
            #print(i,d-i)
            if not (M[i][d-i]==" "):
                incidence = True
            i+=1

        if not incidence:
            return False

    return True

# Prints matrix M
def printMatrix(M):
    print("[")
    for i in range(len(M)):            
        for j in range(len(M[0])):
            print(M[i][j],end="")
        print()
    print("]")

# Adds a horizontal or vertical line to a matrix M
# a = the index at which we would like to place the line
# string = "r" for row, or "c" for column 
def addLine(M,a,string):
    if string=="r":
        for i in  range(len(M)):
            if M[a][i]==" ":
                M[a][i]="-"
            elif M[a][i]=="|":
                M[a][i]="+"
            else:
                print("addLine failed at (",a,i,"), was trying to do",string)
    elif string=="c":
        for i in  range(len(M)):
            if M[i][a]==" ":
                M[i][a]="|"
            elif M[i][a]=="-":
                M[i][a]="+"
            else:
                print("addLine failed at (",i,a,"), was trying to do",string)
    else:
        print("inappropriate string")

################# ALGORITHM STARTS HERE #####################

n=46
print("n =",n)

for x in range(1,int(n/2)+1):
    M = [[" " for x in range(n)] for y in range(n)]
    numberOfLines = 0

    # Try an arithmetic progression with common difference x.
    for i in range(n):
        if i % x == 0:
            addLine(M,i,"c")
            numberOfLines +=1

    if M[0][n-1] == " ":
        addLine(M,n-1,"c")
        numberOfLines += 1

    for j in range(x):
        addLine(M,j,"r")
        numberOfLines += 1
        addLine(M,(n-1)-j,"r")
        numberOfLines += 1

    print("If x =",x,", then y =", numberOfLines)
    printMatrix(M)
    print(incidenceInEveryDiagonal(M))
