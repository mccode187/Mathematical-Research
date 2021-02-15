import itertools

setsThatWork = []
minLen = 3

# Loops through different moduli systems
for m in range(10,11):
    residues = list(range(m))
    #print(residues)

    # Creates a list of all possible residue combinations
    residueCombinations = []
    for L in range(0, len(residues)+1):
        for subset in itertools.combinations(residues, L):
            residueCombinations.append(list(subset))
    #print(residueCombinations)

    # Loops through each possible PAIR of residue combinations
    for combRepeated in residueCombinations:
        for combInitial in residueCombinations:
            # Ignore "badCombos"
            #(when combInitial includes residues that are already included in combRepeated)
            badCombo = False

            for i in combRepeated:
                for j in combInitial:
                    if i==j:
                        badCombo = True

            if not badCombo: 
                # Generate set s
                s = []

                # Add the repeated residue classes
                for i in range(10*m):
                    include = False
                    for j in combRepeated:
                        if i%m == j:
                            include = True

                    if include:
                        s.append(i)

                # Add the initial residue classes
                for i in range(m):
                    for j in combInitial:
                        if i%m == j:
                            include = True

                        if include:
                            s.append(i)
                        
                #print(s)

                # Generate sumset of set s
                sumset = sorted(set(sum(c) for c in itertools.combinations_with_replacement(s, 2)))
                #print(combInitial, combRepeated, s, sumset)
                
                # Checks if the set has propA
                # (in other words, all even numbers are in the sumset)
                propA = True
                for i in range(10*m):
                    if not(2*i in sumset):
                        propA = False

                # Adds to setsThatWork
                if propA and len(combInitial)+len(combRepeated) < m-1:
                    setsThatWork.append([m,combInitial,combRepeated])
            
print(setsThatWork)
