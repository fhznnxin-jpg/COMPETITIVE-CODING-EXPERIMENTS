AIM:
To implement a first-in-first-out (FIFO) queue using only two stacks 
(LIFO structures), supporting the push, pop, peek and empty operations using nothing
but standard stack operations (push to top, pop/peek from top, and size/empty).

TEST CASES:
3. Test Cases
Test Case 1:
Operations: push(1), push(2), peek(), pop(), empty()
Output: 1, 1, false
Explanation: 1 and 2 are enqueued; peek returns the front (1); pop removes and returns 1; the queue still holds 2, so empty returns false.
Test Case 2:
Operations: push(5), pop(), empty()
Output: 5, true
Explanation: 5 is enqueued and then dequeued, leaving the queue empty, so empty returns true.

LEARNING OUTCOMES:
1.Understand the difference between LIFO (stack) and FIFO (queue) behaviour.
2.Learn how to simulate a queue using two stacks with a lazy transfer.
3.Improve logical thinking and problem-solving skills in DSA.
4.Understand amortized O(1) time complexity for the queue operations.
5.Understand implementation in C++, Java, and Python.
