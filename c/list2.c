#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;



int main(void)
{
    //List of size
    node *list = NULL;

    //Add a number to list
    node *n = malloc(sizeof(node));

    if(n ==NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;

    //update list to point to new node
    list = n;

    //Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    list->next = n;

    //Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next=n;

    //Print numbers
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
    //Free list
    while (list != NULL)
    {
        node *tmp = list->next; //armazena o endereço do prox endereço
        free(list);  //libera o primeiro
        list = tmp; //o segundo elemento passa a ser o primeiro, e segue
    }
    return 0;
}