primes = [2]

# Returns whether or not the number a is prime
def isPrime(a):
    primeBoolean = True
    for p in primes:
        if a%p == 0:
            primeBoolean = False
    return primeBoolean

# Checks if a's modular signature is modSig (returns True or False)
def isModSig(a,modSig):
    for i in range(len(modSig)):
        if a%primes[i] != modSig[i]:
            return False
    return True

# Increments modSig by 1 step
def updateModSig(modSig):
    newModSig = modSig.copy()

    i = len(modSig)-1
    keepGoing = True
    while keepGoing:
        if (newModSig[i]==primes[i]-1):
            newModSig[i] = 1
            i = i-1
        else:
            newModSig[i] = newModSig[i] + 1
            keepGoing = False
            
    return newModSig

for i in range(60):
    # Find the next prime
    x = max(primes) + 1

    while not isPrime(x):
        x = x+1
    
    # Check count of modular signature of newly found prime
    modSig = [1]*len(primes)
    count = 1
    while not isModSig(x,modSig):
        modSig = updateModSig(modSig)
        count = count + 1

    print(count)
    
    # Add prime to the prime list
    primes.append(x)

    
    


