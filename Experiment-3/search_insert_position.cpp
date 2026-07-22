#include <iostream>
#include <vector>
using namespace std;
int searchInsert(vector<int>& nums, int target)
{
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
  return left;
}
int main()
{
    int n, target;
    cout << "Enter number of elements: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter sorted array elements:\n";
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    cout << "Enter target element: ";
    cin >> target;
    int index = searchInsert(nums, target);
    cout << "Search Insert Position = " << index << endl;
    return 0;
}
