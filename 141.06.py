#!/usr/bin/python3
'''
Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента, равного n!k!(n−k)!k!(n−k)!n!​.
Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть 
n!=1⋅2⋅3⋅…⋅n
n!=1⋅2⋅3⋅…⋅
Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа или воспользуйтесь уже готовой функцией из модуля math.
'''

from math import factorial
# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))