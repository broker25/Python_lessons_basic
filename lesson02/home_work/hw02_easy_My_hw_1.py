__author__ = 'Сайно Михаил Викторович'
print("Автор ",__author__)

list=["апельсин", "ананас", "мандарин", "груша"]
i=0
for fruit in list:
    i=i+1
    print("{}.{:>30}".format(i,fruit))