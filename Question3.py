## Michael Chu
## 2/9/20

## Question: Given an n by n grid, how many vertical and horizontal lines do
## we need to ensure that there is an intersection ('incidence') in every
## diagonal?

## Equivalent arithmetic combinatorics question:
## Suppose S_1, S_2 are subsets of {0,1,2,...,n-1} and that
## {0,1,2,...,2(n-1)} is a subset of S_1 + S_2.
## How small could |S_1|+|S_2| be?

## Algorithm:
## (1) Generate all sets S containing integers from 0 to n-1.
## (2) For each possible combination of sets S_1 and S_2,
##  generate its sumset, S_1+S_2.
## (3) Find all pairs of sets S_1 and S_2 for which S_1+S_2
##  contains all integers from 0 to 2(n-1).
## (4) Find the smallest value of S_1 + S_2.

## Instruction to user: try running the program with different values of n!

from itertools import chain, combinations

## https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

## (1)
n=12
T=list(range(n))
T_2=list(range(2*(n-1)+1))
sets = list(powerset(T))
#print(sets)

## (2)
set_pairs = []
sumsets = []
for a in range(len(sets)):
    for b in range(len(sets)):
        S_1 = sets[a]
        S_2 = sets[b]
        S_plus_S = []

        ## Compute S+S
        S_plus_S = []
        for i in S_1:
            for j in S_2:
                i_plus_j = i+j
                if not (i_plus_j in S_plus_S):
                    S_plus_S.append(i_plus_j)
        S_plus_S.sort()
        sumsets.append(S_plus_S)
        set_pairs.append((a,b))

## Check if S+S contains T_2
def S_plus_S_contains_T_2(S_plus_S):
    for i in T_2:
        if not (i in S_plus_S):
            return False
    return True

## (3)
valid_set_indices = []
for j in range(len(sumsets)):
    S_plus_S = sumsets[j]
    if S_plus_S_contains_T_2(S_plus_S):
        valid_set_indices.append(j)
        #print(sets[set_pairs[j][0]],sets[set_pairs[j][1]])

## (4)
smallest_valid_set_size = n+n
for i in valid_set_indices:
    set_i_size = len(sets[set_pairs[i][0]]) + len(sets[set_pairs[i][1]])
    if set_i_size < smallest_valid_set_size:
        smallest_valid_set_size = set_i_size

print("n = ",n)
print("Smallest Valid |S_1|+|S_2|: ",smallest_valid_set_size)
for i in valid_set_indices:
    if len(sets[set_pairs[i][0]]) + len(sets[set_pairs[i][1]])==smallest_valid_set_size:
        print(sets[set_pairs[i][0]],sets[set_pairs[i][1]],"\n")
