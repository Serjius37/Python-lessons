/*
*Последовательность 3
*Вывести последовательность чисел, поступившую на вход.
*Входные данные:
*На вход программы поступает последовательность целых чисел. Количество чисел в последовательности заранее неизвестно. Но известно, что в конце последовательности записано число -9999 и в последовательности может быть записано единственное число -9999.
*Выходные данные:
*Вывести все элементы последовательности, кроме заключительного -9999, на экран. 
*/

#include <stdio.h>

int main() 
{
    int control;
    while(control != -9999) {
        scanf("%d", &control);
        if (control != -9999) 
            printf("%d ", control);
    }
    return 0;
}