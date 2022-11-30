/*Возрастающая последовательность 2
Модернизировать программу, написанную на прошлом шаге так, чтобы программа выдавала число 0, если последовательность возрастающая, либо номер элемента последовательности, нарушающего возрастание.
Входные данные:
Последовательность целых чисел. Признак окончания последовательности - число -9999.
Выходные данные:
Число 0 -- если последовательность возрастающая. Число kk -- если последовательность не является возрастающей. kk -- номер первого члена последовательности, которые нарушает возрастание. 
*/

#include <stdio.h>

int main() {
    int f = 0, a = -1, c = -32768, w = 1,d = 0;
    for (; a!= -9999;) {
        scanf ("%d", &a);
        if (a == -9999) break;
        if (a <= c && w == 1) {
            f += 1;
            w = d;
        }
        c=a;
        d += 1;
    }        
    
     if (f) {
        printf ("%d",w+1);
     } else { 
        printf("0");
    }    
    return 0;
}