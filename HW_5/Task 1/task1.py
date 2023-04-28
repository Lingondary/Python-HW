# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


print("Программа возводит A в степень B.")

def Exp(A, B):
    if B == 0:
        return 1
    return A * Exp(A, B-1)

print("Введите A:")
A = int(input())
print("Введите B:")
B = int(input())

print(Exp(A, B))