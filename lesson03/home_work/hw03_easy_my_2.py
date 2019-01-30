# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

def lucky_ticket(ticket_number):
    stroka = str(ticket_number)
    sum_beg=0
    sum_end=0
    mid = int(len(stroka)/2)
    for i in range(mid):
        sum_beg += int(stroka[i])
        sum_end += int(stroka[i])
    return sum_beg == sum_end

print(lucky_ticket(12321))
print(lucky_ticket(436751))

