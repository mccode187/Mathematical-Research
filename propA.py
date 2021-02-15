import itertools

setsThatWork = []
minLen = 3

# Loops through different moduli systems
for m in range(2,11):
    residues = list(range(m))
    #print(residues)

    # Creates a list of all possible residue combinations
    residueCombinations = []
    for L in range(0, len(residues)+1):
        for subset in itertools.combinations(residues, L):
            residueCombinations.append(list(subset))
    #print(residueCombinations)

    # Loops through each residue combination
    for comb in residueCombinations:
        # Generate set s
        s = []
        for i in range(10*m):
            include = False
            for j in comb:
                if i%m == j:
                    include = True

            if include:
                s.append(i)

        # Make sure that 0 is always automatically included
        if not(0 in s):
            s.append(0)
            
        #print(s)

        # Generate sumset of set s
        sumset = sorted(set(sum(c) for c in itertools.combinations_with_replacement(s, 2)))
        #print(sumset)
        
        # Checks if the set has propA
        propA = True
        for i in range(10*m):
            if not(2*i in sumset):
                propA = False

        if propA and len(comb) <= minLen:
            setsThatWork.append([m,[comb]])
            
print(setsThatWork)
