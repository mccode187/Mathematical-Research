## Michael Chu
## 2/15/20

## Question: Given an n by n grid, how many vertical and horizontal lines do
## we need to ensure that there is an intersection ('incidence') in every
## diagonal?

## Equivalent arithmetic combinatorics question:
## Suppose S_1, S_2 are subsets of {0,1,2,...,n-1} and that
## {0,1,2,...,2(n-1)} is a subset of S_1 + S_2.
## How small could |S_1|+|S_2| be?

## Instruction to user: try running the program with different values of n!

import itertools

n=14
T=list(range(n))
T_2=list(range(2*(n-1)+1))
print(T)
print(T_2)

k=0
keepTrying = True
while keepTrying:
    print(k)
    def S_plus_S_contains_T_2(S_plus_S):
        for i in T_2:
            if not (i in S_plus_S):
                return False
        return True

    def pairThatWorks(k):
        for i in range(int(k/2)+1):
            # Generate all subsets of T of size i
            subsetsOfSize_i = list(itertools.combinations(T, i))
            # Generate all subsets of T of size k-i
            subsetsOfSize_k_minus_i = list(itertools.combinations(T, k-i))

            for S_1 in subsetsOfSize_i:
                for S_2 in subsetsOfSize_k_minus_i:
                    # Generate S_plus_S, the sumset of S_1 and S_2
                    S_plus_S = []
                    for i in S_1:
                        for j in S_2:
                            i_plus_j = i+j
                            if not (i_plus_j in S_plus_S):
                                S_plus_S.append(i_plus_j)
                    S_plus_S.sort()

                    # Check if the sumset contains all integers from 0 to 2(n-1)
                    # If the sumset does contain all those integers, return True
                    #print(S_1,S_2,S_plus_S)
                    if S_plus_S_contains_T_2(S_plus_S):
                        return True
        # If, out of all possible pairs of subsets such that |S_1|+|S_2| = k,
        # we could not find a pair that works, then return False
        return False
    
    if pairThatWorks(k):
        keepTrying = False
        print("n =",n)
        print("Smallest Valid |S_1|+|S_2|:",k)
    else:
        k+=1
