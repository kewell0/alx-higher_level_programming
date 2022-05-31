#include "lists.h"

/**
 * check_cycle - check for loop in
 * linked list
 *
 * @list : linked list head
 * Return: 0 OR 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *str = list;

	while (ptr && str && str->next)
	{
		ptr = ptr->next;
		str = str->next->next;
		if (str == ptr)
		{
			return (1);
		}
	}
	return (0);
}
