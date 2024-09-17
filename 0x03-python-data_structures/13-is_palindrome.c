#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the start of the list
 * Return: Pointer to the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;

    while (head != NULL)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the start of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
    listint_t *mid_node = NULL; // To handle odd size case
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    // Find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handle odd-sized list
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half
    second_half = reverse_list(slow);
    prev_slow->next = NULL; // Null terminate the first half

    // Compare the first and second halves
    listint_t *first_half = *head;
    listint_t *second_half_copy = second_half; // To restore later
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the list (reverse back the second half)
    second_half_copy = reverse_list(second_half_copy);
    if (mid_node != NULL) // Odd case, attach the middle node
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half_copy;
    }
    else
    {
        prev_slow->next = second_half_copy;
    }

    return (is_palindrome);
}
