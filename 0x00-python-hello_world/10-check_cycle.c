#include "lists.h"

/**
 * check_cycle - check if a singly list has a cycle in it
 * list: the singly list
 * Description:only write printf putchar puts malloc and free
 * Return: 0 if none and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *woman = list;
	listint_t *man = list;

	if (!list)
		return (0);

	while (woman && man && man->next)
	{
		woman = woman->next;
		man = man->next->next;
		if (woman == man)
			return (1);
	}

	return (0);
}
