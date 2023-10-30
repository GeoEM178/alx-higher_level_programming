#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *batia = list;
	listint_t *sarii = list;

	if (!list)
		return (0);

	while (batia && sarii && sarii->next)
	{
		batia = batia->next;
		sarii = sarii->next->next;
		if (batia == sarii)
			return (1);
	}

	return (0);
}
