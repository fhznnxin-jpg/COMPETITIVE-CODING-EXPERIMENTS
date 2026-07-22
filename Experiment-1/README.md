Experiment 1
Aim
Contains Duplicate

Problem Statement
Given an integer array nums and an integer k, return true if there are two distinct indices i and j such that:

nums[i] == nums[j]
abs(i - j) <= k
Otherwise, return false.

Approaches Implemented
1. Brute Force
Compare every element with every other element.
If duplicate elements are found within distance k, return true.
Time Complexity: O(n²)

Space Complexity: O(1)

2. Hashing (Optimal)
Use an unordered_map to store the latest index of each element.
If the element is already present and the index difference is less than or equal to k, return true.
Time Complexity: O(n)

Space Complexity: O(n)

3. Sliding Window
Use an unordered_set to maintain a window of the last k elements.
If the current element already exists in the window, return true.
Time Complexity: O(n)

Space Complexity: O(min(n, k))

Files
BruteForce.cpp
HashingOptimal.cpp
SlidingWindow.cpp
Output
Output screenshots are available in the Outputs folder.
