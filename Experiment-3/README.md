Experiment 4  
Search Insert Position

Aim
Implement Binary Search to find the index of a target element in a sorted array. If the target is not found, return the position where it should be inserted.

Algorithm
1. Initialize left and right pointers.
2. Find the middle element.
3. Compare the target with the middle element.
4. Search the appropriate half.
5. Return the insertion position if not found.

Time Complexity
O(log n)

Space Complexity
O(1)

Sample Input
4
1 3 5 6
2

Sample Output
Search Insert Position = 1
