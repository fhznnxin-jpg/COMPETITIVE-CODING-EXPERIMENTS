#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    if (source == destination) return true;
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(source);
    visited[source] = true;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int next : adj[node]) {
            if (next == destination) return true;
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
    return false;
}
 
int main() {
    vector<vector<int>> edges = {{0,1},{1,2},{2,0}};
    cout << (validPath(3, edges, 0, 2) ? "true" : "false") << endl;
    return 0;
}
