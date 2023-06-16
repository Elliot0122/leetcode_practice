class Solution {
public:
    int math(string numa, string numb, string operatorr){
        int num1 = stoi(numa);
        int num2 = stoi(numb);
        char operatorrr = operatorr[0];
        switch(operatorrr){
            case '+':
                return num1+num2;
            case '-':
                return num1-num2;
            case '*':
                return num1*num2;
            case '/':
                return num1/num2;
            default:
                return 0;
        }
    }
    int evalRPN(vector<string>& tokens) {
        vector<string> popped;
        while(!tokens.empty()){
            if(tokens.size() == 1 && popped.empty())break;
            string temp1, temp2, op;

            temp1 = tokens.back();
            tokens.pop_back();
            if(temp1 == "+" || temp1 == "-" || temp1 == "*" || temp1 == "/"){
                popped.push_back(temp1);
            }else{
                temp2 = popped.back();
                if(temp2 == "+" || temp2 == "-" || temp2 == "*" || temp2 == "/"){
                    popped.push_back(temp1);
                }else{
                    popped.pop_back();
                    op = popped.back();
                    popped.pop_back();
                    stringstream stream;
                    stream << math(temp1, temp2, op);
                    stream >> temp1;
                    tokens.push_back(temp1);
                }
            }
        }
        return stoi(tokens.back());
    }
};
