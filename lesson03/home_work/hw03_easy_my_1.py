# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

def my_round(number, ndigits):
    number = number*(10**ndigits)
    left = number%1
    number = number//1 # no abs allowed
    if number>0 and left>=0.5: # if number<0&float(left)<=-0.5:
        number += 1
    else:
	    if number<0 and left<=-0.5:
		    number-=1
    return number/(10**ndigits)


#print(0.67>=0.5)
print(my_round(2.1234567, 5))
print(my_round(-2.48888888, 5))
print(my_round(2.9999967, 5))
