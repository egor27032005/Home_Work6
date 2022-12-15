length=int(input())
mas=[int(input()) for i in range(length)]
sum=0
for index, length in enumerate(mas):
   if index%2==1:
      sum+=length
print(mas)
print(sum)
##Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции