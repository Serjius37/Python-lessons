/*Измените программу, написанную на прошлом шаге таким образом, чтобы каждое число выводилось столько раз, каково его значение. Например, число 5 5 5 должно выводиться 5 5 5 раз.
Входные данные:
Два натуралных числа A,B, A,B, A,B, таких, что B>A. B \gt A. B>A.

Выходные данные:
A A A чисел A A A , A+1 A+1 A+1 чисел A+1 A+1 A+1 и т.д. Каждое число занимает поле шириной в 4 символа.*/

#include <stdio.h>

int main() {
    int k,m;
    scanf ("%d %d",&k,&m);
    if (m<=0){
      printf("");  
    } else {
        if (k<0){
            for (int i = 1; i!=m+1; i+=1){  
                for(int j = 1; j<=i; j+=1){
                    printf("%4.d",i); 
                }    
            } 
        } else {
            for (int i = k; i!=m+1; i+=1){   
                for(int j = 1; j<=i; j+=1){
                    printf("%4.d",i);  
                }        
            } 
         }
    } return 0;
}