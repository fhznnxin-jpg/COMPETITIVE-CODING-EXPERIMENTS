#include <iostream>
#include <vector>
using namespace std;
vector<int>Self(vector<int>& nums)
{
    int n=nums.size();
    vector<int>answer(n);
    for(int i=0;i<n;i++)
    {
        int product=1;
        for(int j=0;j<n;j++)
        {
            if(i!=j)
            {
                product=product*nums[j];
            }
        }
        answer[i]=product;
    }
    return answer;
}
int main()
{
    int n;
    cout<<"Enter size of array: ";
    cin>>n;
    vector<int>nums(n);
    cout<<"Enter elements: ";
    for(int i=0; i<n; i++)
        cin>>nums[i];
    vector<int>result=Self(nums);
    cout<<"Output: ";
    for(int i=0;i<n;i++)
        cout<<result[i]<< " ";
    return 0;
}
