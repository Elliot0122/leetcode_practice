class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        pair<int, int> p;
        p.first = val;
        p.second = (stack.empty())? val: min(val, stack.back().second);
        stack.push_back(p);
    }
    
    void pop() {
        stack.pop_back();
    }
    
    int top() {
        return stack.back().first;
    }
    
    int getMin() {
        return stack.back().second;
    }
private:
    vector<pair<int, int>> stack;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
