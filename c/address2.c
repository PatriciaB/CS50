#include <stdio.h>
#include <cs50.h>

int main(void)
{
    /*
    string s = "HI!";   //char *s = "HI!";   //igual a string s, pq indica o inicio da string
    char *p = &s[0];
    printf("%p\n", p);
    printf("%p\n", s);      //the address of the first caracter

    */


    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));    //  printf("%c\n", s[1]);
    printf("%c\n", *(s+2));     // printf("%c\n", s[2]);
}