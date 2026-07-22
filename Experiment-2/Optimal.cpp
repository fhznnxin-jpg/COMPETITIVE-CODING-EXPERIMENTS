#include <iostream>
#include <vector>
using namespace std;
vector<int>optimal(vector<int>& nums)
{
    int n=nums.size();
    vector<int>answer(n);
    answer[0]=1;
    for (int i=1;i<n;i++)
    {
        answer[i]=answer[i-1]*nums[i-1];
    }
    int right=1;
    for (int i=n-1;i>=0;i--)
    {
        answer[i]=answer[i]*right;
        right = right*nums[i];
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
    for(int i=0; i<n; i++)
        cin>>nums[i];
    vector<int>result =optimal(nums);
    cout <<"Output: ";
    for (int x:result)
        cout<< x << " ";
    return 0;
}
