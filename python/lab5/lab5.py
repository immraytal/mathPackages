import numpy as np
import math as ma
import matplotlib.pyplot as plt
import random

fileName = './files/first'

f = open(fileName)
lines = f.readlines()
f.close()
arrCoeff = []
arrFree = []

for line in lines:
    row = []
    temp = []
    for numb in line:
        if numb == ' ':
            row.append(''.join(temp))
            temp = []
            continue
        temp.append(numb)
        for i in range(len(row)):
            row[i] = int(row[i])
    arrCoeff.append(row)

for line in lines:
    arrFree.append(int(line[-2]))

print(arrCoeff)
print(arrFree)

answ = np.linalg.solve(arrCoeff, arrFree)

f = open('answers.txt', 'w')
for i in range(len(arrFree)):
    f.write('x' + str(i+1) + ' = ' + str(answ[i])+ '\n')
f.close()

def ThirdFirst(a, b):
    try:

        if b == '1':
            return round(random.random() * (float(a[1]) - float(a[0])) + float(a[0]), 2)
        elif b == '2':
            return random.randint(int(a[0]), int(a[1]))
    except:
        print('Неверно введенные значения')

print('Получите псевдослучайное четное число в пределах от 6 до 12')
a = list(input('Введите диапазон от и до через ПРОБЕЛ\n>').split())
b = input('Выберите нужно число\n1. Вещественное\n2. Целое\n>')
print(ThirdFirst(a, b))


def ThirdSecond(a, b):
    try:
        while (True):
            temp = ThirdFirst(a, b)
            if temp % 5 != 0:
                temp = None
            else:
                return temp
    except:
        print('Неверно введенные значения')
print('Также получите число кратное пяти в пределах от 5 до 100')
a = list(input('Введите диапазон от и до через ПРОБЕЛ\n>').split())
b = input('Выберите нужно число\n1. Вещественное\n2. Целое\n>')
print(ThirdSecond(a, b))


def RandVectors(n):
    try:
        a = []
        a.append(random.random() * 2)
        a.append(random.random() * 100)
        b = '1'
        answer1 = []
        answer2 = []
        answer3 = []
        for i in range(n):
            answer1.append(ThirdFirst(a, b))
            answer2.append(random.normalvariate(random.random()*5, random.random()))
            answer3.append(int(ThirdFirst(a, b)))
        print(answer1 , '\n' , answer2, '\n' , answer3)
    except:
        print('Неверно введенные значения')

print('Генерация массивов случайных чисел')
n = int(input('Введите кол-во значений'))
RandVectors(n)

def Fifth():
    x = np.arange(-6, 6, 0.1)  # диапазон
    y = x ** 2 - x - 6  # парабола
    r = np.random.normal(0, 2, len(x))  # белый шум
    z = y + r
    a = np.ones((len(x), 3))
    a[:, 1] = x
    a[:, 2] = x ** 2
    result = np.linalg.lstsq(a, z)
    za = np.dot(a, result[0])  # аппроксимирующая кривая
    plt.plot(x, z, 'o ', color='green')
    plt.plot(x, za, color='red')
    print((result[1] / len(x)))  # ошибка аппроксимации
    plt.show()

Fifth()