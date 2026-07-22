#include <iostream>
#include <vector>
using namespace std;
bool Duplicate(vector<int>& nums, int k)
{
    int n=nums.size();
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(nums[i] == nums[j] && (j - i) <= k)
            {
                return true;
            }
        }
    }
    return false;
}
int main()
{
    int n,k;
    cout<<"Enter size of array: ";
    cin>>n;
    vector<int>nums(n);
    cout<<"Enter elements: ";
    for (int i=0;i<n;i++)
        cin>>nums[i];
    cout<<"Enter k: ";
    cin>>k;
    if(Duplicate(nums, k))
        cout<<"true";
    else
        cout<<"false";
    return 0;
}
