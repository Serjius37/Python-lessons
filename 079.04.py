 /*Дубликаты
Удалить из последовательности дубликаты.
Входные данные:
В первой строке задано натуральное число NN. Во второй строке записана упорядоченная по возрастанию последовательность из NN целых чисел, которая может содержать одинаковые элементы.
Выходные данные:
Вывести все различные элементы последовательности, упорядоченные по возрастанию.
*/

#include <stdio.h>

int main() {
    int w, a, c = 0;
    scanf ("%d", &w);
    for (int k=w; k; k--) {
        scanf ("%d", &a);
        if (a == c) continue;{
            c = a;
            printf("%d ",a);
        }
    }    
    return 0;
}