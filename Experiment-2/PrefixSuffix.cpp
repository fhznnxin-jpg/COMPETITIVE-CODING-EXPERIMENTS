#include <iostream>
#include <vector>
using namespace std;
vector<int>prefixsufix(vector<int>& nums)
{
    int n=nums.size();
    vector<int>answer(n, 1);
    int prefix=1;
    for(int i=0;i<n;i++)
    {
        answer[i]=prefix;
        prefix=prefix*nums[i];
    }
    int suffix=1;
    for (int i=n-1;i>=0;i--)
    {
        answer[i]=answer[i]*suffix;
        suffix=suffix*nums[i];
    }
    return answer;
}
int main()
{
    int n;
    cout<<"Enter size: ";
    cin>>n;
    vector<int>nums(n);
    cout<<"Enter elements: ";
    for(int i=0;i<n;i++)
        cin>>nums[i];
    vector<int>result=prefixsufix(nums);
    cout<<"Output: ";
    for(int x:result)
        cout<<x<< " ";
    return 0;
}
