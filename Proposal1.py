## Michael Chu
## 1/26/20

## Choose some positive integer n.
## Let T = {k | 0<=k<=2^n}
## Let S = {0}.
## Add {2^k | k>=0, 2^k<=2^n} to S.
## Add {3^k | k>=0, 3^k<=2^n} to S.
## Add {4^k | k>=0, 4^k<=2^n} to S.
## Continue this process until S+S contains T.

## Test:

n=11
big_power = 2**n
S_plus_S = []

def S_plus_S_contains_T():
    ## Check if S+S contains T
    for i in T:
        if not (i in S_plus_S):
            return False
    return True

## Compute T
T = []
for k in range(big_power + 1):
    T.append(k)
#print(T,"\n")

S = [0]
a = 1
while not S_plus_S_contains_T():
    ## Compute S
    a+=1
    k = 0
    power = a**k
    while power <= big_power:
        if not (power in S):
            S.append(power)
        k+=1
        power = a**k
    S.sort()
    ## print(S,"\n")

    ## Compute S+S
    S_plus_S = []
    for i in S:
        for j in S:
            i_plus_j = i+j
            if not (i_plus_j in S_plus_S):
                S_plus_S.append(i_plus_j)
    S_plus_S.sort()
    ## print(S_plus_S,"\n")
print(S)
print(S_plus_S_contains_T(),"\n")
