# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms

n1,n2 = int(input("What is the first integer?")), int(input("What is the second integer?"))
MaxVal = int(input("What is the highest value term?"))


def FibSUm(n1,n2,MaxVal):
    KeepGoing = True
    ListEven = []
    count = 0
    if n1 % 2 == 0:
        ListEven.append(n1)
    if n2 % 2 == 0:
        ListEven.append(n2)
    while KeepGoing:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        if nth % 2 == 0:
            ListEven.append(nth)
        if n1 + n2 > MaxVal:
            KeepGoing = False
    print(sum(ListEven))
    # or
    ListEvenSum = 0
    for i in ListEven:
        ListEvenSum += i
    print(ListEvenSum)

FibSUm(n1,n2,MaxVal)




