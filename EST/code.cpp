#include <iostream>
#include <vector>
using namespace std;
int searchInsert(const vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
int main() {
    int n;
    cout << "Enter array size: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter " << n << " sorted distinct integers: ";
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    int target;
    cout << "Enter target: ";
    cin >> target;
    cout << "Result index: " << searchInsert(nums, target) << '\n';
    return 0;
}
