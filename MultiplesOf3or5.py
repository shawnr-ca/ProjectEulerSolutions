# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

Multiples3or5List = []

for num in range(1000):
    if num%3 == 0 or num%5 == 0:
        Multiples3or5List.append(num)

print(sum(Multiples3or5List))

# or

sumofMult = 0
for num in Multiples3or5List:
    sumofMult += num
print(sumofMult)