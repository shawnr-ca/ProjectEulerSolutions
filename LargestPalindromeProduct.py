# Find the largest palindrome made from the product of two 3-digit numbers.

NumbDig = int(input("What are the number of digits for both integers you would like to find the largest possible palindrome between their products?"))


LargestNum = int(str(9)*NumbDig)**2
LargestNumDig = int(str(9)*NumbDig)
SmallestNum = int((str(1) + str(0)*(NumbDig-1)))**2
SmallestNumDig = int((str(1) + str(0)*(NumbDig-1)))
PossNums = []

for i in range(SmallestNumDig, LargestNumDig + 1):
    for j in range(SmallestNumDig, LargestNumDig + 1):
        PossNums.append(i*j)

PalList = []

for i in PossNums:
    #Since all single digit # are palindromes
    if len(str(i)) == 1:
        PalList.append(i)
    # Odd number digit Palindrome
    if len(str(i)) % 2 != 0:
        PalDigCount = 0
        for j in range(1, int((len(str(i))-1)/2) + 1):
            if str(i)[j-1] == str(i)[-j]:
                PalDigCount += 1
            if PalDigCount == (len(str(i))-1)/2:
                PalList.append(i)
    # Even number digit Palindrome
    if len(str(i)) % 2 == 0:
        PalDigCount = 0
        for j in range(1, int((len(str(i))) / 2) + 1):
            if str(i)[j - 1] == str(i)[-j]:
                PalDigCount += 1
            if PalDigCount == int((len(str(i))) / 2):
                PalList.append(int(i))



print(PalList)
