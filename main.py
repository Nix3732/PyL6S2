import csv
import random
import os


def show(option, digit):
    d = digit
    if digit == '':
        d = 5
    d = int(d)

    if len(data) - 1 <= 5 <= d:
        for i in range(1, len(data) - 1):
            print(data[i])
        print('Cтрок недостаточно')
        option = ' '

    if option == 'top' or option == '':
        b = []
        for i in range(0, len(data[0])):
            a = []
            for j in range(0, d):
                a.append(len(str(data[j][i])))
            b.append(a)

        for i in range(0, d + 1):
            for j in range(0, len(data[0])):
                print(str(data[i][j]).center(max(b[j])), end=' ')
            print("\n")

    if option == 'bottom':
        b = []
        for i in range(0, len(data[0])):
            a = []
            for j in range(len(data) - d, len(data)):
                a.append(len(str(data[j][i])))
            b.append(a)

        for j in range(0, len(data[0])):
            print(str(data[0][j].center(max(b[j]))), end=' ')
        print("\n")
        for i in range(len(data) - d, len(data)):
            for j in range(0, len(data[0])):
                print(str(data[i][j]).center(max(max(b[j]), len(str(data[0][j])))), end=' ')
            print("\n")

    if option == 'random':
        n = sorted(random.sample(range(1, len(data) + 1), d))
        b = []
        for i in range(0, len(data[0])):
            a = []
            for j in range(len(n)):
                a.append(len(str(data[j][i])))
            b.append(a)

        for j in range(0, len(data[0])):
            print(str(data[0][j].center(max(b[j]))), end=' ')
        print("\n")
        for i in range(0, len(n) - 1):
            for j in range(0, len(data[0])):
                print(str(data[n[i]][j]).center(max(max(b[j]), len(str(data[0][j])))), end=' ')
            print("\n")


def info():
    stroki = len(data) - 1
    stolbsi = len(data[0])
    print(f"{stroki}x{stolbsi}")

    value = []
    for i in range(0, len(data[0])):
        counter = 0
        for j in range(1, len(data)):
            if data[j][i] != '':
                counter += 1
        value.append(counter)

    tp = None
    for i in range(1, len(data[0])):
        counter = 0
        for j in range(0, len(data)):
            if data[j][i] != '':
                counter += 1
            if counter == len(data[0]):
                tp = data[j]
                break
        if counter == len(data[0]):
            break
    types = ["int", "int", "int", "str", "str", "float", "int", "int", "str", "float", "str", "str"]

    for i in range(0, len(data[0])):
        print(data[0][i], value[i], types[i])


# def delnan():

file = open('Titanic.csv', 'r')
data = csv.reader(file)

data = list(data)

# show(input('top, bottom, random\n'), input('int\n'))
# info()
