## Michael Chu
## 2/7/20

## Question: How many subsets S of {0,1,2,...,n} satisfy the property that
## {0,1,2,...,n} is a subset of S+S?

## Algorithm:
## (1) Generate all sets S containing integers from 0 to n.
## (2) For each possible set S, generate its sumset, S+S.
## (3) Find all sets S for which S+S contains all integers from 0 to n.
## (4) Count how many sets there are.

## Instruction to user: try running the program with different values of n!

from itertools import chain, combinations

## https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

## (1)
n=10
T=list(range(n+1))
sets = list(powerset(T))

## (2)
sumsets = []
for i in range(len(sets)):
    S = sets[i]
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
        
print("n = ",n)
print("Number of subsets that work: ",len(valid_set_indices))
print("Number of subsets that DON'T work: ",len(sets)-len(valid_set_indices))
print("Percentage of subsets that work: ", len(valid_set_indices)/len(sets))
#for i in valid_set_indices:
 #   print(sets[i])
