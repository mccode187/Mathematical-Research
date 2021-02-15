## Michael Chu
## 1/28/20

## Question: Suppose I want my sumset S+S to contain all integers from 0 to n.
## How small can S be?

## Algorithm:
## (0) Set |S| = ceiling(set_size_lower_bound)
## (1) Generate all sets S of size |S| containing integers from 0 to n.
## (2) For each possible set S, generate its sumset, S+S.
## (3) Find sets S for which S+S contains all integers from 0 to n.
## (4a) If we find no such sets, increment |S| by 1 and go back to step (1).
## (4b) If we do find such sets, print them out.
## (5) END

## Instruction to user: try running the program with different values of n!

from itertools import combinations
import math

## (0)
n=5
set_size_lower_bound = -1/2 + math.sqrt(2*n+1/4)
print("Set Size Lower Bound:",set_size_lower_bound)

T=list(range(n+1))

set_size = math.ceil(set_size_lower_bound)-1
# ^may want to subtract 1 just to be a little cautious

number_of_sets_checked = 0
found_sets_that_work = False
while not found_sets_that_work:
    ## (1)
    sets_to_consider = list(combinations(T, set_size))
    print(sets_to_consider)
    ## (2)
    sumsets = []
    for i in range(len(sets_to_consider)):
        S = sets_to_consider[i]
        S_plus_S = []
        
        ## Compute S+S
        S_plus_S = []
        for i in S:
            for j in S:
                i_plus_j = i+j
                if not (i_plus_j in S_plus_S):
                    S_plus_S.append(i_plus_j)
        S_plus_S.sort()
        
        sumsets.append(S_plus_S)

    ## Check if S+S contains T
    def S_plus_S_contains_T():
        for i in T:
            if not (i in S_plus_S):
                return False
        return True

    ## (3)
    valid_set_indices = []
    for j in range(len(sumsets)):
        S_plus_S = sumsets[j]
        if S_plus_S_contains_T():
            valid_set_indices.append(j)
            
    ## (4)
    if len(valid_set_indices) > 0:
        print("n =",n)
        print("Smallest Valid Set Size: ",set_size)
        for i in valid_set_indices:
            print(sets_to_consider[i])
        found_sets_that_work = True
    else:
        set_size += 1

    number_of_sets_checked += len(sets_to_consider)

print("Number of Sets Checked: ",number_of_sets_checked)
