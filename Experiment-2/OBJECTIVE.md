Experiment 2
Title
Product of Array Except Self

Problem Statement
Given an integer array nums, return an array answer such that:

answer[i] is equal to the product of all the elements of nums except nums[i].
Do not use the division operator.
Solve the problem in O(n) time.
Approaches Implemented
1. Brute Force
For every element, multiply all the remaining elements.
Store the product in the answer array.
Time Complexity: O(n²)

Space Complexity: O(n)

2. Prefix & Suffix Arrays
Compute the prefix product for every index.
Compute the suffix product for every index.
Multiply both values to get the final answer.
Time Complexity: O(n)

Space Complexity: O(n)

3. Optimal (Prefix Array + Right Variable)
Store only the prefix products in the output array.
Traverse from right to left using a single variable right.
Multiply the prefix product with the running right product.
Time Complexity: O(n)

Space Complexity: O(1) (excluding the output array)

Files
BruteForce.cpp
PrefixSuffix.cpp
Optimal.cpp
Output
Output screenshots are available in the Outputs folder.
