import math

# String builder

set1 = []
sumset = []
wait = 0

for i in range(50):
    evenNum = 2*i
    wait = i*math.log(i+1)*0.1
    if not evenNum in sumset:
        j = -1
        count = 0
        appended = False
        while not appended:
            j += 1
            if j+j == evenNum:
                count += 1
            else:
                for element in set1:
                    if element + j == evenNum:
                        count +=1
        
            if count >= wait:    
                set1.append(j)
                appended = True

        # Update sumset
        for element in set1:
            theSum = element + j
            if (theSum % 2 == 0) and not theSum in sumset:
                sumset.append(theSum)

print(set1)
print(sumset)
                
