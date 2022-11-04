//uso de ponteiros

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;     //ponteiro, onde fica armazenado o endereço da variavel
    printf("%p\n", p);          // mostrar onde esta a variavel

    printf("%p\n", &n);         // mostrar onde esta a variavel
    printf("%i\n", *p);     //mostrar numero que esta naquele endereco



}