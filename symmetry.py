# Michael Chu
# 10/23/20

# Checks if binary string s satisfies 1-symmetry condition
# s must be of odd length
# 0 represents composite, 1 represents prime
def symmetry(s):
    len(s)
    middle = int((len(s)-1)/2)
    for i in range(middle+1):
        primePair = False
        for j in range(i+1):
            if s[i-j] == "1" and s[i+j] == "1":
                primePair = True
        if primePair == False:
            return False
    return True

# Test

#1101010001010
#print(symmetry("11100101000010010000001"))

# Adds 1 to a binary string
# *Note: cannot add 1 to a binary string consisting of all 1's
def plusOne(s):
    newS = s
    if s[(len(s)-1)] == "0":
        newS = newS[:len(s)-1] + "1"
    else:
        one = True
        index = len(s)-1
        while one:
           newS = newS[:index] + "0" + newS[index+1:]
           index = index-1
           if newS[index] == "0":
               newS = newS[:index] + "1" + newS[index+1:]
               one = False
    return newS

# Test
##print(plusOne("00000"))
##print(plusOne("00001"))
##print(plusOne("00010"))
##print(plusOne("00011"))
##print(plusOne("01101"))

# Generates all binary strings and checks if they satisfy symmetry property
# n must be odd
def genAll(n):
    s = "0" * n
    passes = 0
    fails = 0
    for k in range(2**n):
        if(symmetry(s)):
            passes = passes + 1
            print(s + " pass "+str(passes))
        else:
            #print(s + " fail")
            fails = fails + 1
        s = plusOne(s)

    total = passes+fails
    print()
    print("Passes: "+str(passes))
    print("Fails: "+str(fails))
    print("Total: "+str(total))
    print()
    print("Percent Passes: "+str(passes/total))
    print("Percent Fails: "+str(fails/total))

# Test
#genAll(13)

# Generates all binary strings and checks if they satisfy symmetry property
# AND having "11" other than the first two chars is not allowed
# n must be odd
def genAllNo11(n):
    s = "0" * n
    passes = 0
    fails = 0
    for k in range(2**n):
        if( not ("11" in s[1:]) and symmetry(s) ):
            passes = passes + 1
            print(s + " pass " + passes)
        else:
            #print(s + " fail")
            fails = fails + 1
        s = plusOne(s)

    total = passes+fails
    print()
    print("Passes: "+str(passes))
    print("Fails: "+str(fails))
    print("Total: "+str(total))
    print()
    print("Percent Passes: "+str(passes/total))
    print("Percent Fails: "+str(fails/total))

# Test
#genAllNo11(11)

# Generates all binary strings and checks if they satisfy symmetry property
# prints only half of the string, however
# n must be odd
def genAllHalf(n):
    s = "0" * n
    passes = 0
    fails = 0
    passList = []
    for k in range(2**n):
        if(symmetry(s)):
            passes = passes + 1
            if not (s[:int((n-1)/2)+1] in passList):
                passList.append(s[:int((n-1)/2)+1])
        else:
            #print(s + " fail")
            fails = fails + 1
        s = plusOne(s)

    for i in range(len(passList)):
        print(passList[i] + " pass " + str(i+1))
        
    total = passes+fails
    print()
    print("Passes: "+str(passes))
    print("Fails: "+str(fails))
    print("Total: "+str(total))
    print()
    print("Percent Passes: "+str(passes/total))
    print("Percent Fails: "+str(fails/total))

# Test
#genAllHalf(13)


# Starts with a base, then adds 0's unless forced to add a 1.
def genString(base, numDigitsToAdd):
    string = base
    for i in range(numDigitsToAdd):
        testString = string+"0"+len(string)*"1"
        if symmetry(testString):
            string = string+"0"
        else:
            string = string+"1"
    return string

print(genString("1111111",50))
