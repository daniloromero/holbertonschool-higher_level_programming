#include "list.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list for checking cycles
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *liebre = head, *tortuga = head;

	if (head != NULL)
		tortuga = tortuga->next;
		liebre = tortuga->next;


