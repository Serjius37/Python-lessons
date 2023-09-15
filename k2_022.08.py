#!/usr/bin/python3
'''
Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.
Формат входных данных
На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.
Формат выходных данных
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.
Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.
'''
a = input()
b = input()
if a == b:
    print("ничья")
elif a == "камень" and (b == "ножницы" or b == "ящерица"):
    print("Тимур")
elif a == "ножницы" and (b == "бумага" or b == "ящерица"):
    print("Тимур")
elif a == "бумага" and (b == "камень" or b == "Спок"):
    print("Тимур")
elif a == "ящерица" and (b == "бумага" or b == "Спок"):
    print("Тимур")
elif a == "Спок" and (b == "камень" or b == "ножницы"):
    print("Тимур")    
else:
    print("Руслан")