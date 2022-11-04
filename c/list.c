#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //Dymanically allocate
    int *list = malloc(3 * sizeof(int));            //memoria dinamica, 3 vezes o tamanho de um int
    if (list == NULL)
    {
        return 1;
    }
    // assign three numberrs
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    int *tmp = realloc(list, 4 * sizeof(int));  //realoca e libera memoria
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }
    tmp[3] = 4;

    //liberar memoria sempre que usar malloc

for(int i=0; i<3; i++)
    {
        printf("%i\n", list[i]);
    }

    //liberar memoria sempre que usar malloc
  //  free(list);
}