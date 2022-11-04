#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s+1));          //tamanho que precisa para armazenar, 1 a mais por causa do espaço em branco no final
    if(t == NULL)   //algo deu errado, nao confie nas informações
    {
        return 1;
    }

    strcpy(t,s);        //copia da variavel s para t

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);   //primeira maiuscula
    }
    printf("s: %s\n", s);           //quando se copia uma string, copia o ponteiro, aponta para o mesmo lugar
    printf("t: %s\n", t);
}