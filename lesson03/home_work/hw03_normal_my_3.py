
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)


def func(x):
    if x > 0:
        return 1
    else:
        return 0

def my_filter(fun, ar):
    back=[]
    #print(arg)
    #print(arg[1])
    for i in range(len(ar)):
        #print(arg[i])
        if fun(ar[i]):
            back.append(ar[i])
    return back

a = [1, -4, 6, 8, -10]
print (my_filter(func,a))