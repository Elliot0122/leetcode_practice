class Solution {
public:
    static bool comparison(string a, string b){
        return a+b > b+a;
    }
    vector<string> to_str(vector<int> nums){
        vector<string> newVec;
        for(auto i:nums)
            newVec.push_back(to_string(i));
        return newVec;
    }
    string largestNumber(vector<int>& nums) {
        vector<string> newVec = to_str(nums);
        sort(newVec.begin(), newVec.end(), comparison);
        if(newVec[0] == "0") return "0";
        string ans = "";
        for(string s:newVec){
            ans += s;
        }
        return ans;
    }
};
