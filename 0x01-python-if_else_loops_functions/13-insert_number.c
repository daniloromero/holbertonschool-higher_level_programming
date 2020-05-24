#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the linked list
 * @number: data to be interted
 * Return: Address of the new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *aux = *head, *aux2;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!aux || aux->n >= number)
	{
		new_node->next = aux;
		*head = new_node;
		return (new_node);
	}
	aux2 = aux->next;
	while (aux && aux2 && aux2->n < number)
	{
		aux = aux->next;
		aux2 = aux->next;
	}
	aux->next = new_node;
	new_node->next = aux2;
	return (new_node);
}
