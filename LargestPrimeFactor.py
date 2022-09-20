# What is the largest prime factor of the number 600851475143 ?

import time

Num = int(input("What number is being searched for its largest prime factor?"))

def LargestPrimeFact(Num):
    NumFact = []
    PrimeNumFact = []
    if Num % 2 == 0:
        LargestPossFact = int(Num/2)
    else:
        LargestPossFact = int((Num-1)/2)
    for i in range(1, LargestPossFact + 1):
        if Num % i == 0 and i != 1:
            NumFact.append(i)
    for i in NumFact:
        Prime = True
        MultCount = 0
        for j in range(2,i):
            if i % j == 0:
                MultCount += 1
        if MultCount > 0:
            Prime = False
        if Prime == True:
            PrimeNumFact.append(i)
    if len(PrimeNumFact) == 0:
        print(Num)
    else:
        print(max(PrimeNumFact))


start = time.time()
LargestPrimeFact(Num)
end = time.time()
TotalTime = end - start
print(TotalTime)