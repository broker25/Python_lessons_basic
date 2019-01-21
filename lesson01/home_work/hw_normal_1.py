# Задание 1

__author__ = 'Сайно Михаил Викторович'

x = input('Введите ваше число ')
max=0
for letter in str(x):
    if int(letter)>max:
        max=int(letter)
print("Макс цифра",max)
print("Автор ",__author__)
