#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    char *s = get_string("s: ");            //get_string sempre é um ponteiro, indicando o inicio da string
    char *t = get_string("t: ");

    if(strcmp(s,t) == 0)            //se sao iguais, retorna zero, comparacao de string
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }

}