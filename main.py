import csv
import random
import os


def show(option, digit, da):
    d = digit
    if digit == '':
        d = 5
    d = int(d)

    if len(da) - 1 <= 5 <= d:
        for i in range(1, len(da) - 1):
            print(da[i])
        print('Cтрок недостаточно')
        option = ' '

    if option == 'top' or option == '':
        b = []
        for i in range(0, len(da[0])):
            a = []
            for j in range(0, d):
                a.append(len(str(da[j][i])))
            b.append(a)

        for i in range(0, d + 1):
            for j in range(0, len(da[0])):
                print(str(da[i][j]).center(max(b[j])), end=' ')
            print("\n")

    if option == 'bottom':
        b = []
        for i in range(0, len(da[0])):
            a = []
            for j in range(len(da) - d, len(da)):
                a.append(len(str(da[j][i])))
            b.append(a)

        for j in range(0, len(da[0])):
            print(str(da[0][j].center(max(b[j]))), end=' ')
        print("\n")
        for i in range(len(da) - d, len(da)):
            for j in range(0, len(da[0])):
                print(str(da[i][j]).center(max(max(b[j]), len(str(da[0][j])))), end=' ')
            print("\n")

    if option == 'random':
        n = sorted(random.sample(range(1, len(da) + 1), d))
        b = []
        for i in range(0, len(da[0])):
            a = []
            for j in range(len(n)):
                a.append(len(str(da[j][i])))
            b.append(a)

        for j in range(0, len(da[0])):
            print(str(da[0][j].center(max(b[j]))), end=' ')
        print("\n")
        for i in range(0, len(n) - 1):
            for j in range(0, len(da[0])):
                print(str(da[n[i]][j]).center(max(max(b[j]), len(str(da[0][j])))), end=' ')
            print("\n")


def info(d):
    stroki = len(d) - 1
    stolbsi = len(d[0])
    print(f"{stroki}x{stolbsi}")

    value = []
    for i in range(0, len(d[0])):
        counter = 0
        for j in range(1, len(d)):
            if d[j][i] != '':
                counter += 1
        value.append(counter)

    typesa = []
    for i in range(1, len(d)):
        typesb = []
        for j in range(0, len(d[0])):
            counter = 0
            counter1 = 0
            flag = False
            for a in d[i][j]:
                if a in '0123456789':
                    counter += 1
            for a in d[i][j]:
                if a in '0123456789.':
                    counter1 += 1
            for a in d[i][j]:
                if a.lower() in 'qwertyuiopasdfghjklzxcvbnm':
                    flag = True
            if flag is True:
                typesb.append("str")
            else:
                if counter == len(d[i][j]):
                    typesb.append("int")
                else:
                    if counter1 == len(d[i][j]):
                        typesb.append("float")
        typesa.append(typesb)
    types = []
    for i in range(0, len(d[0])):
        cint = 0
        cstr = 0
        cfloat = 0
        for j in range(0, len(typesa)):
            if typesa[j][i] == 'int':
                cint += 1
            if typesa[j][i] == 'float':
                cfloat += 1
            if typesa[j][i] == 'str':
                cstr += 1
        if cstr == 0:
            if cfloat == 0:
                types.append('int')
            else:
                types.append('float')
        else:
            types.append('str')

    for i in range(0, len(d[0])):
        print(d[0][i], value[i], types[i])


def delnan(d):
    output = []
    for i in range(0, len(d)):
        counter = 0
        for j in range(0, len(d[0])):
            if data[i][j] == '':
                counter += 1
        if counter == 0:
            output.append(d[i])
    return output


def makeds(d):
    value = len(d)-1
    learn = int(value * 0.7)
    lrn = sorted(random.sample(range(1, value+1), learn))
    tst = []
    for i in range(1, value+1):
        if i not in lrn:
            tst.append(i)
    os.makedirs('workdata/learning')
    os.makedirs('workdata/testing')
    train = open('workdata/learning/train.csv', 'w', newline='')
    test = open('workdata/testing/test.csv', 'w', newline='')
    trainwriter = csv.writer(train)
    testwriter = csv.writer(test)
    for i in lrn:
        trainwriter.writerow(d[i])
    for i in tst:
        testwriter.writerow(d[i])


file = open('Titanic.csv', 'r')
data = csv.reader(file)
data = list(data)

"""
data - начальный набор данных
lst - будет очищенный от строк с пустыми ячейками
"""
# lst = delnan(data)

# show(input('top, bottom, random\n'), input("int\n"), lst)

# info(data)

# makeds(data)
