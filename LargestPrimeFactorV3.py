from math import sqrt
import time

#Num = int(input("What number is being searched for its largest prime factor?"))

def LargestPrimeFact(Num):
    if Num == 0 or Num < 0:
        return "no"
    elif Num == 1:
        return 1
    else:
        # Even
        while Num % 2 == 0:
            prime = 2
            Num /= 2
        # Odd
        for i in range(3, int((sqrt(Num) + 1))):
            while Num % i == 0:
                prime = i
                Num /= i
        if Num > 2:
            prime = Num
        return int(prime)

Number = int(input("Up to what number do would you like to see the primes?"))

start = time.time()

Primes = []
LenBetPrimes = []
LenBetPrimes1 = []

for i in range(Number):
    Primes.append((LargestPrimeFact(i), i))

PrimesinRangeX = []
for i in Primes:
    if i[0] == i[1]:
        PrimesinRangeX.append(i[0])

for i in range(1,len(PrimesinRangeX)):
    LenBetPrimes.append((PrimesinRangeX[i]-PrimesinRangeX[i-1],str(str(PrimesinRangeX[i]) + "-" + str(PrimesinRangeX[i-1] ))))
    LenBetPrimes1.append(PrimesinRangeX[i] - PrimesinRangeX[i - 1])

end = time.time()
TotalTime = end - start

print("The primes in range of 0 to " + str(Number) + " are "+ str(PrimesinRangeX))
print("The distance between the primes in in range of 0 to " + str(Number) + " are " + str(LenBetPrimes))
print("/ " + str(LenBetPrimes1))
print("The greatest distance between two primes is " + str(max(LenBetPrimes1)) + " between integers " + str(PrimesinRangeX[LenBetPrimes1.index(max(LenBetPrimes1))]) + " and " + str(PrimesinRangeX[LenBetPrimes1.index(max(LenBetPrimes1)) + 1]))
print("The time it took to execute this is prime search is: " + str(TotalTime) + " seconds")

