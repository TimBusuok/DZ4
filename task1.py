# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

n = int(input('введите число '))
m = int(input('введите число: '))
list_1 = set()
list_2 = set()

ans = True
for i in set(range(0, n)):
    list_1.add(random.randint(0, 10))
    ans = False
ans = True
for j in set(range(0, m)):
    list_2.add(random.randint(0, 10))
    ans = False

same_num = list_1.intersection(list_2)

print(list_1)
print(list_2)
print(same_num)

