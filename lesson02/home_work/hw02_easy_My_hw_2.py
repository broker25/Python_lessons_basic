__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

list1=["апельсин", "ананас", "мандарин", "груша"]
list2=["апельсин", "ананас", "манго", "финик"]
i=0
while i<len(list1):
    if list1[i] in list2:
        list1.pop(i)
    else:
        i+=1
print(list1)