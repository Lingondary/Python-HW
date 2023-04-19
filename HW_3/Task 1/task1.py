#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

print("Программа вычисляет сколько раз встречается число X в случайном массиве длины N.\nЕсли такого числа нет, ближайшее к N число.\nВведите N:")
N = int(input())
print("Введите искомое число X: ")
X = int(input())

A = [random.randint(0,10) for i in range(N)]


def counter(int, list):
    counter = 0
    for i in list:
        if i == int:
            counter += 1
    return counter

def closest_num(int, list):
    output = 10
    temp = 10
    for i in list:
        if abs(i - int) < temp:
            temp = abs(i - int)
            output = i
    return output

def result_output():
    if counter(X, A) > 0:
        print(counter(X, A))
    else:
        print("Ближайшее число: " + str(closest_num(X,A)))
    

print(A)
result_output()