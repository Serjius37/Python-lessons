#!/usr/bin/python3
'''
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

a = int(input())
i  = j = l = 0
w = 0
array = ['w'] * a
while a != i:
    d = int(input())
    array[i] = d
    i += 1
while a != j:
    if array[j] < 0:
        print(array[j])
    j += 1
while a != l:
    if array[l] == 0:
        print(array[l])
    l += 1 
while a != w:
    if array[w] > 0:
        print(array[w])
    w += 1 