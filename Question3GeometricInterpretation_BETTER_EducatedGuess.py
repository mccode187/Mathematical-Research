## Michael Chu
## 3/4/20

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
            print(i,d-i)
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
                incidenceInDiagonal[a+i]=True
            else:
                print("addLine failed at (",a,i,"), was trying to do",string)
    elif string=="c":
        for i in  range(len(M)):
            if M[i][a]==" ":
                M[i][a]="|"
            elif M[i][a]=="-":
                M[i][a]="+"
                incidenceInDiagonal[i+a]=True
            else:
                print("addLine failed at (",i,a,"), was trying to do",string)
    else:
        print("inappropriate string")

################# ALGORITHM STARTS HERE #####################

n=9
M = [[" " for x in range(n)] for y in range(n)]
numberOfLines = 0
incidenceInDiagonal = [False]*(2*n-1)

if n>0:
    addLine(M,0,"r")
    numberOfLines += 1
    addLine(M,0,"c")
    numberOfLines += 1

if n>1:
    addLine(M,n-1,"r")
    numberOfLines += 1
    addLine(M,n-1,"c")
    numberOfLines += 1

## Loop through all the diagonals (no need to loop through the central diagonal)
for k in range(n-1):
    # Loop through diagonal in the northwest half of the grid
    # AND
    # Loop through diagonal in southeast half of the grid
    for d in [k,(2*n-2)-k]:
        print(d)
        
        ## If there is a box in diagonal d containing a "+", we're good and can move
        ##        on to the next diagonal.
        ## But if there's no box containing a "+", we need to consider all of the
        ##        boxes containing "|" or "-".
        if not incidenceInDiagonal[d]:
            # Initialize the variables that keep track of the max.
            maxCount = -1
            maxDim = "r"
            if d<=n-1:
                maxIndex = 0
            elif d>=n:
                maxIndex = d-(n-1)

            ## Loop through all possible boxes in diagonal d
            for i in range(n-abs(d-(n-1))):
                if d<=n-1:
                    r=i
                    c=d-i
                elif d>=n:
                    r=d-(n-1)+i
                    c=(n-1)-i

                ## Check if the box contains a "|"
                if M[r][c]=="|":
                    ## See what happens if we add a horizontal line through this
                    ## box; that is, count number of vertical lines.
                    count=0
                    for j in range(n):
                        if M[r][j]=="|" and (not incidenceInDiagonal[r+j]):
                            count+=1
                    if count > maxCount:
                        maxCount = count
                        maxDim = "r"
                        maxIndex = r
                        
                ## Check if the box contains a "-"
                elif M[r][c]=="-":
                    ## See what happens if we add a vertical line through this
                    ## box; that is, count number of horizontal lines.
                    count=0
                    for j in range(n):
                        if M[j][c]=="-" and (not incidenceInDiagonal[j+c]):
                            count+=1
                    if count > maxCount:
                        maxCount = count
                        maxDim = "c"
                        maxIndex = c

            ## Place a line that maximizes the number of "+"'s created
            addLine(M,maxIndex,maxDim)
            numberOfLines += 1
        printMatrix(M)

print("n =",n)
print(numberOfLines,"lines")
printMatrix(M)
