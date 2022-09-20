# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MinNum = int(input("What is the first number in the range of numbers which are all factors of the number being calculated?"))
MaxNum = int(input("What is the second number in the range of numbers which are all factors of the number being calculated?"))


def SmallestEvenDivNum(MinNum,MaxNum):
    Mults = []
    if MinNum == 0:
        MinNum += 1
    Num = 1
    for i in range(MinNum,MaxNum + 1):
        Num *= i
        Mults.append((i,Num))
    for i in range(1,len(Mults)):
        Div1 = []
        Div2 = []
        for j in range(1,Mults[i][0] + 1):
            if Mults[i][0] % j == 0:
                Div1.append(j)
            if Mults[i-1][1] % j == 0:
                Div2.append(j)
            DivCom = [1]
            for k in Div1:
                for h in Div2:
                    if k == h:
                        DivCom.append(k)
            if ((Mults[i][0] * Mults[i - 1][1])/(max(DivCom))) < Mults[i][1]:
                Mults1 = list(Mults)
                Mults1[i] = (Mults[i][0],int((Mults[i][0] * Mults[i - 1][1])/((max(DivCom)))))
                Mults = tuple(Mults1)

    return max(Mults)[1]





print(SmallestEvenDivNum(MinNum,MaxNum))

