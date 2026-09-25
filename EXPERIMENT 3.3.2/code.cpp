#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {

                if (grid[r][c] == '1') {
                    dfs(grid, r, c, m, n);
                    count++;
                }
            }
        }

        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int r, int c, int m, int n) {

        // Check boundary and water
        if (r < 0 || r >= m || c < 0 || c >= n ||
            grid[r][c] != '1') {
            return;
        }

        // Mark current land as visited
        grid[r][c] = '0';

        // Visit up
        dfs(grid, r - 1, c, m, n);

        // Visit down
        dfs(grid, r + 1, c, m, n);

        // Visit left
        dfs(grid, r, c - 1, m, n);

        // Visit right
        dfs(grid, r, c + 1, m, n);
    }
};

int main() {

    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };

    Solution obj;

    int result = obj.numIslands(grid);

    cout << "Number of Islands: " << result << endl;

    return 0;
}
