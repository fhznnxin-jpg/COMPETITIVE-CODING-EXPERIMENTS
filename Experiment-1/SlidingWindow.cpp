#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool containsNearbyDuplicate(vector<int>& nums, int k)
{
    unordered_set<int> window;

    for (int i = 0; i < nums.size(); i++)
    {
        if (window.count(nums[i]))
            return true;

        window.insert(nums[i]);

        if (window.size() > k)
            window.erase(nums[i - k]);
    }

    return false;
}

int main()
{
    int n, k;

    cout << "Enter size: ";
    cin >> n;

    vector<int> nums(n);

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> nums[i];

    cout << "Enter k: ";
    cin >> k;

    if (containsNearbyDuplicate(nums, k))
        cout << "Output: true";
    else
        cout << "Output: false";

    return 0;
}
