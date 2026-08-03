Problem 1
Easy  |  Linked List  Two Pointers  Stack  Recursion
1. Problem Statement
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
A linked list is a palindrome if it reads the same forward as it does backward — i.e., the sequence of node values from head to tail is identical to the sequence from tail to head.
Input Format
•	The head of a singly linked list (1 <= number of nodes <= 100,000)
•	Each node value: 0 <= Node.val <= 9
Output Format
•	Return true if the linked list is a palindrome, false otherwise.
Constraints
•	The number of nodes in the list is in the range [1, 10^5].
•	0 <= Node.val <= 9
Note:  A follow-up challenge is to solve it in O(n) time and O(1) extra space. The O(1) space solution requires modifying the list in place by reversing the second half, then restoring it — handle this carefully in a real system.
