## Michael Chu
## 1/26/20

## Let S = {0} U {2^k | 0<=k, 2^k<=3^n} U {3^k | 0<=k<=n}
## Let T = {k | 0<=k<=3^n}
## Guess: S+S contains T

## Test:

n=5

## Compute S
S = [0]
for k in range(n):
    S.append(3**k)
k=0
while 2**k <= 3**n:
    S.append(2**k)
    k+=1
S.sort()
print(S,"\n")

## Compute S+S
S_plus_S = []
for i in S:
    for j in S:
        i_plus_j = i+j
        if not (i_plus_j in S_plus_S):
            S_plus_S.append(i_plus_j)
S_plus_S.sort()
print(S_plus_S,"\n")

## Compute T
T = []
for k in range(3**n + 1):
    T.append(k)
#print(T,"\n")

## Check if S+S contains T
S_plus_S_contains_T = True
for i in T:
    if not (i in S_plus_S):
        S_plus_S_contains_T = False
    
print(S_plus_S_contains_T,"\n")
