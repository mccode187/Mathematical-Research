primes = [2]

# Returns whether or not the number a is prime
def isPrime(a):
    primeBoolean = True
    for p in primes:
        if a%p == 0:
            primeBoolean = False
    return primeBoolean

for i in range(60):
    # Find the next prime
    x = max(primes) + 1

    while not isPrime(x):
        x = x+1
    
    # Add prime to the prime list
    primes.append(x)

numberOfPrimes = 4
primorial = 1

# Primorial
for i in range(numberOfPrimes):
    primorial = primorial * primes[i]

numbers = list(range(primorial))
sievedNumbers = numbers.copy()

print(numbers)

#Sieve
for i in range(numberOfPrimes):
    multiplier = 0
    while multiplier*primes[i] < len(sievedNumbers):
        sievedNumbers[multiplier*primes[i]] = -1
        multiplier += 1

print(sievedNumbers)

#Blocks
blocks = []
count = 0
for i in range(len(sievedNumbers)):
    if sievedNumbers[i] == -1:
        count+=1
    else:
        blocks.append(count)
        count = 0

print(blocks)
print(len(blocks))
