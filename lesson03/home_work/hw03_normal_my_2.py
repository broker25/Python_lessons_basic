# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

def my_sort(ar):
    for i in range(len(ar)-1):
        #print("i=",i)
        for j in range(0,len(ar)-1):
            #print("j=",j)
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]
    #print(ar)
    return ar

a = [1, -4, 6, 8, -10]
print (my_sort(a))