import numpy

primes = [2]

# Returns whether or not the number a is prime
def isPrime(a):
    primeBoolean = True
    for p in primes:
        if a%p == 0:
            primeBoolean = False
    return primeBoolean

# Loop through 1 prime, 2 primes, 3 primes, ...
for i in range(6):
    m = numpy.prod(primes)
    largestK = 0
    print("-------"+"PRIMES: "+str(primes))
    # Loop through all the residues mod m
    for r in range(m):
        # Search for a k value that gives us a gap on the left and right
        k=0
        search = True
        while search:
            foundK = True
            for p in primes:
                if ((r+k)%p == 0) or ((r-k)%p == 0):
                    foundK = False
            if foundK:
                search = False
            else:
                k = k+1
        #print("r = "+str(r)+": k = "+str(k))
        #print(str(k))
        if k>largestK:
            largestK = k
    print(largestK)
    # Find the next prime
    x = max(primes) + 1

    while not isPrime(x):
        x = x+1

    # Add prime to the prime list
    primes.append(x)
