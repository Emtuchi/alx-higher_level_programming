#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to the singly linked list
 * Return: 0 if cycle doesnt exist, 1 if it exists
 */

int check_cycle(listint_t *list)
{
	listint_t *present_list = list;

	while (present_list->next)
	{
		if ((present_list->next) == list)
			return (1);

		present_list = present_list->next;
	}
	return (0);
}
