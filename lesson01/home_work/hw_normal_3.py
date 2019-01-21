# Задание 3 normal

__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)
import math
a=float(input('Введите коэф a'))
b=float(input('Введите коэф b'))
c=float(input('Введите коэф c'))

d=b**2.0-4.0*a*c

if d>0:
    print("Первый корень равен",(-b+math.sqrt(d))/2.0/a)
    print("Второй корень равен",(-b-math.sqrt(d))/2.0/a)
else:
    print("Действительных корней нет")