class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        int ans = nums[0];
        int temp_max = nums[0];
        for(int i=1; i<len; ++i){
            temp_max+=nums[i];
            temp_max = max(temp_max, nums[i]);
            ans = max(temp_max, ans);
        }
        return ans;
    }
};
