## 1.Найти сумму чисел списка стоящих на нечетной позиции

n = 5
x = 1
numbers = list(range(0, n))

for i in numbers :
    x= x*-3
    print(x)


## 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
## Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

from random import randint
import math

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) ==1: results.append(numbers[0]**2)
    return results

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

n = 9
frst = 1
last = 10

mylist = get_numbers(n, frst, last)
print(mylist)
mylist = get_numbers(n, frst, last)
print(pairs_mult(mylist))

# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
## Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def get_real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
mynums = get_real_nums(n, frst, last)

print (mynums)
print(find_diff(mynums))


# 4. Написать программу преобразования десятичного числа в двоичное

n = int(input('Введите число: '))

def dec_to_bin(n):
    bin = ''
    while n > 1:
        bin += str(n % 2)
        n = n // 2
    return bin[::-1]

print(dec_to_bin(n))


