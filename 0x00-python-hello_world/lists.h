#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
/**
 *struct listint_s - singly linked list
 *@n: integer
 *@next: points to the next node
 *Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

/**
  *print_listint - prints all elements of a listint_t list
  *@h: pointer to the lists head
  *Return: number of nodes
  */
size_t print_listint(const listint_t *h);

/**
  *add_nodeint - adds a new node at the beginning
  *of a listint_t list
  *@head: pointer to a pointer of the start of the list
  *@n: integer to be included in the node
  *Return: address of the new element or NULL if it fails
  */
listint_t *add_nodeint(listint_t **head, const int n);
/**
  *free_listint - frees a listint_t list
  *@head: pointer to list to be freed
  *Return: void
  */
void free_listint(listint_t *head);
/**
  *check_cycle - checks if a singly linked list has a cycle
  *@list: pointer to the head of the list
  *Return: 1 if there is a cycle, 0 if there is no cycle
  */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
