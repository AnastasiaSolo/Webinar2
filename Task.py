# Найти сумму чисел списка стоящих на нечетной позиции.
N = int(input('Inter number:'))
aList = list(range(1, N+1))
print(aList)


def SumOddPosition(aList):
    return sum(aList[1::2])

print(SumOddPosition(aList))

#Найти произведение пар чисел в списке.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д

N = int(input('Inter number:'))
aList = list(range(1, N+1))
print(aList)

import math
def SumOddPosition(aList):
    Produkt = []
    for i in range(math.ceil(len(aList)/2)):
     Produkt.append(aList[i] * aList[-i-1])
    return (Produkt)
print(SumOddPosition(aList))

# 24. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов

from random import uniform

def GetRealNums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def diff(nums):
    nums = [round(x - int(x), 2) for x in (nums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
nums = GetRealNums(n, frst, last)

print (nums)
print(diff(nums))

#Написать программу преобразования десятичного числа в двоичное
a = int(input('inter number: '))
result = []

while a:
    result.append(a % 2)
    a //= 2
result.reverse()
print(int(''.join(map(str, result))))