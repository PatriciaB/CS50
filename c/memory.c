#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3* sizeof(int));         //espaço suficiente para 3 bits
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;

    free(x);        //libera espaço no final

}