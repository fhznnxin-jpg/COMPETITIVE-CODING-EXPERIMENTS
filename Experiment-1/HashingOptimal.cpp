#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
bool Duplicate(vector<int>& nums, int k)
{
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); i++)
    {
        if (mp.count(nums[i]))
        {
            if (i - mp[nums[i]] <= k)
                return true;
        }
        mp[nums[i]] = i;
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
        cout << "true";
    else
        cout << "false";
    return 0;
}
