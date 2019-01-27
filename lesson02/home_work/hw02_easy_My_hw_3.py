__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

list1=[2,3,4,8,9,12,20,21]
list2=[]
for el in list1:
    if el%2==0:
        list2.append(el/4.0)
    else:
        list2.append(el*2.0)
print(list2)
