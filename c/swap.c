#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);       //passa o endereço das variaveis, ponteiros
    printf("x is %i, y is %i\n", x, y);
}



void swap(int *a, int *b)         //como envia o ponteiro, consegue alterar, senao passa só uma copia
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}