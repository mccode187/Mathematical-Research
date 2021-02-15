## Michael Chu
## 1/26/20

## Let S = {0} U {all perfect powers less than a^n}
## Let T = {k | 0<=k<=a^n}
## Guess: S+S contains T

## Test:

n=10
a=2

## http://oeis.org/A001597
perfect_powers = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1000, 1024, 1089, 1156, 1225, 1296, 1331, 1369, 1444, 1521, 1600, 1681, 1728, 1764]

## Compute S
S = [0]
for k in range(a**n + 1):
    if k in perfect_powers:
        S.append(k)
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
for k in range(a**n + 1):
    T.append(k)
#print(T,"\n")

## Check if S+S contains T
S_plus_S_contains_T = True
for i in T:
    if not (i in S_plus_S):
        S_plus_S_contains_T = False
    
print(S_plus_S_contains_T,"\n")
