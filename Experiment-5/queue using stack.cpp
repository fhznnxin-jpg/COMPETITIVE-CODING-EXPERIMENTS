#include <iostream>
#include <stack>
using namespace std;
class MyQueue {
    stack<int> input, output;
    void transfer() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
    }
public:
    void push(int x) { input.push(x); }
    int pop() {
        transfer();
        int front = output.top();
        output.pop();
        return front;
    }
    int peek() {
        transfer();
        return output.top();
    }
    bool empty() {
        return input.empty() && output.empty();
    }
};
int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    cout << q.peek() << endl;
    cout << q.pop() << endl;
    cout << (q.empty() ? "true" : "false") << endl;
    return 0;
}
