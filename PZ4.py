#4. Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

n = int(input('Пользователь, введите целое положительне число n: '))
maxi = 0
A = True

while (A == True):
    buf = n % 10
    if (maxi<buf):
        maxi = buf
    n//=10
    if (n==0):
        A = False
print('Самая большая цифра в числе', maxi)
