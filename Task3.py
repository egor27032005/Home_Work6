length=int(input())
mas=[int(input()) for i in range(length)]
if length%2==0:
  half=length//2
else:
   half=length//2+1
mas2=[mas[i]*mas[-i-1] for i in range(half)]
print(mas)   
print(mas2)
##Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.