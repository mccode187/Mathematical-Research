# Symmetry Left Pair

primes = [2]

# Returns whether or not the number a is prime
def isPrime(a):
    primeBoolean = True
    for p in primes:
        if a%p == 0:
            primeBoolean = False
    return primeBoolean

for i in range(1000):
    # Find the next prime
    x = max(primes) + 1

    while not isPrime(x):
        x = x+1
        
    # Add prime to the prime list
    primes.append(x)

for n in range(2,1000):
    keepSearching = True
    i = 0;
    while keepSearching:
        for j in range(len(primes)):
#            print(primes[i],primes[j],2*n)
            if primes[i] + primes[j] == 2*n:
                keepSearching = False
                #print(str(primes[i]))
                print(str(primes[i])+"+"+str(primes[j])+"="+str(2*n))
                break
        i = i+1
