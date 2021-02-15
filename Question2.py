## Michael Chu
## 2/5/20

## Question: Is there a quadratic sequence that covers all the natural #s with
## its sumset?

## Algorithm:

## Tip: try changing numberOfTimes! (and n if you want)

n=25
numberOfTimes = 6
S = [0]

## Generate sequence S
count = 0
step = 1
for i in range(n*numberOfTimes):
    S.append(S[i]+step)
    count += 1
    if count == numberOfTimes:
        step += 1
        count = 0
        
print(S)

## Compute S+S
S_plus_S = []
for i in S:
    for j in S:
        i_plus_j = i+j
        if not (i_plus_j in S_plus_S):
            S_plus_S.append(i_plus_j)
S_plus_S.sort()

## Check if S+S covers all natural numbers up to the biggest
## element of S

T=list(range(max(S)+1))

def S_plus_S_contains_T():
    for i in T:
        if not (i in S_plus_S):
            print(i,i/max(S))
            return False
    return True

print(S_plus_S_contains_T())
