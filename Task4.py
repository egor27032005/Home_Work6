length=int(input())
mas=[float(input()) for i in range(length)]
print(mas)
print(round((max(mas,key=lambda x:x%1)-min(mas,key=lambda x:x%1))%1,1))
#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.