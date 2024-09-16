'''
На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
Формат входных данных 
На вход программе подается строка генетического кода, состоящая из символов А, Г, Ц, Т, а, г, ц, т.
Формат выходных данных
Программа должна вывести сколько гуанина, тимина, цитозина, аденина входит в данную строку генетического кода.
Примечание. Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.
'''

s = input()
s = s.lower() 
print('Аденин:',s.count('а'))
print('Гуанин:',s.count('г'))
print('Цитозин:',s.count('ц'))
print('Тимин:',s.count('т'))