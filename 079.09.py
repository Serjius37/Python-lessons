/*
Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
Входные данные:
Отсутствуют
Выходные данные:
См.пример выходных данных 
*/

#include <stdio.h>

int main() {
    int a;
    for (a=1; a != 101; a++) {
        if (a % 15 == 0) {
            printf ("FizzBuzz ");
        }else if(a % 3 == 0) {
            printf ("Fizz ");
        }else if(a % 5 == 0) {
            printf ("Buzz ");
        }else {
            printf ("%d ", a);
        }    
    }
    return 0;
}