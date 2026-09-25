#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        vector<int> dp(amount + 1, amount + 1);

        dp[0] = 0;

        for (int a = 1; a <= amount; a++) {

            for (int c : coins) {

                if (c <= a) {
                    dp[a] = min(dp[a], dp[a - c] + 1);
                }
            }
        }

        return dp[amount] <= amount ? dp[amount] : -1;
    }
};

int main() {

    vector<int> coins = {1, 2, 5};
    int amount = 11;

    Solution obj;

    int result = obj.coinChange(coins, amount);

    cout << "Minimum number of coins: " << result << endl;

    return 0;
}
