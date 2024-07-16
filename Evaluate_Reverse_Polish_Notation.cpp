//https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> stack;
        int a, b;
        
        for (const std::string& token : tokens) {
            if (token == "+") {
                a = stack.top();
                stack.pop();
                b = stack.top();
                stack.pop();
                stack.push(b + a);
            } else if (token == "-") {
                a = stack.top();
                stack.pop();
                b = stack.top();
                stack.pop();
                stack.push(b - a);
            } else if (token == "*") {
                a = stack.top();
                stack.pop();
                b = stack.top();
                stack.pop();
                stack.push(b * a);
            } else if (token == "/") {
                a = stack.top();
                stack.pop();
                b = stack.top();
                stack.pop();
                stack.push(b / a);
            } else {
                stack.push(std::stoi(token));
            }
        }
        
        return stack.top();
    }
};