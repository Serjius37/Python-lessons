'''
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
Формат входных данных 
На вход программе подается строка.
Формат выходных данных
Программа должна вывести количество буквенных символов в нижнем регистре.
'''

s = input()
count = 0
for i in s:
    if i != i.upper():
        count += 1
print(count)