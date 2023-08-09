#include "lists.h"

/**
 * check_cycle -> checks if a singly linked list has a cycle in it.
 * @list: the list to be checked.
 *
 * Return: 0 if there is no cycle, 1 if otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	if (list == 0)
		return (0);

	a = list;
	b = list;

	while (a && b && a->next)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
			return (1);
	}
	return (0);
}
