/*Кнопочный электронный кодовый замок имеет десять кнопок. Каждая из кнопок имеет свой порядковый номер от 0 до 9. Правильный код 1024 зашит внутрь замка. Человек, который хочет открыть дверь, должен ввести на циферблате последовательно 1, 0, 2 и 4. Напишите программу, моделирующую работу такого замка.
Входные данные:
Четыре целых числа b1,b2,b3,b4 b_1,b_2,b_3, b_4 b1​,b2​,b3​,b4​ -- номера кнопок, которые нажал человек.
Выходные данные:
Строка open, если введён правильный код. Строка close, если введён неправильный код. */

#include <stdio.h>

int main() {
    int a,b,c,d;
    scanf("%d %d %d %d",&a,&b,&c,&d);
    if (a==1 && b==0 && c==2 && d==4) {
      printf("open");
    } else
      printf("close");
    return 0;
}