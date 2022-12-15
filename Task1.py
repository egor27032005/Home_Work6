length=int(input())
mas=[int(input()) for i in range(length)]
print(mas)
mas.sort()
print(mas)
lst=[mas[i] for i in range(length-1) if mas[i]!=mas[i+1] and mas[i]!=mas[i-1]]
if mas[length-1]!=mas[length-2]:
    lst.append(mas[length-1])
print(lst)
#3 Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.