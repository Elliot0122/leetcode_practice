class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans = {0}, exp = {1};
        int cnt = 0;
        while(cnt < n){
            int size = exp.size();
            for(int i=0; i<size; ++i){
                if(cnt == n)break;
                ans.push_back(exp[i]);
                exp.push_back(exp[i]+1);
                cnt++;
            }
        }
        return ans;
    }
};
// 0  1  1 2  1 2 2 3  1 2 2 3 2 3 3 4 
