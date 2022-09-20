import time
Num = int(input("What number is being searched for its largest prime factor?"))

def LargestPrimeFact(n):
    x = 2
    FactList = []
    if n == 0 or n < 0:
        print("no")
    elif n == 1:
        print(1)
    else:
        while n > 1:
            if n % x == 0:
                FactList.append(n)
                n /= x
            elif n % x != 0:
                x += 1

        print(int(FactList[-1]))

start = time.time()
LargestPrimeFact(Num)
end = time.time()
TotalTime = end - start
print(TotalTime)


