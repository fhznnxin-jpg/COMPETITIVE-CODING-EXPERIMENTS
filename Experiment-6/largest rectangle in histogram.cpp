#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<int> stk;
        int maxArea = 0;
        for (int i = 0; i < heights.size(); i++) {
            while (!stk.empty() && heights[stk.top()] > heights[i]) {
                int height = heights[stk.top()];
                stk.pop();
                int left = stk.empty() ? -1 : stk.top();
                int width = i - left - 1;
                maxArea = max(maxArea, height * width);
            }
            stk.push(i);
        }
        heights.pop_back();
        return maxArea;
    }
};
int main() {
    Solution obj;
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    cout << obj.largestRectangleArea(heights) << endl;
    return 0;
}
