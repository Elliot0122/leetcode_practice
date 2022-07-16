class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int len = nums.size();
        int temp = 1;
        for(int i=0; i<len; ++i){
            ans.push_back(temp);
            temp*=nums[i];
        }
        temp = 1;
        for(int i=len-1; i>=0; --i){
            ans[i]*=temp;
            temp*=nums[i];
        }
        return ans;
    }
};
