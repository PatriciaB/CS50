#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("s: ");

    string t = s;

    t[0] = toupper(t[0]);   //primeira maiuscula

    printf("s: %s\n", s);           //quando se copia uma string, copia o ponteiro, aponta para o mesmo lugar
    printf("t: %s\n", t);           // mostra a string

    printf("s: %p\n", s);           //mostra o ponteiro
    printf("t: %p\n", t);
}