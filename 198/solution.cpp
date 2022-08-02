class Solution {
public:
    int rob(vector<int>& nums) {
        int s = nums.size();
        if(s == 1)return nums[0];
        else if(s == 2)return max(nums[0], nums[1]);
        else if(s == 3)return max(nums[0]+nums[2], nums[1]);
        int dp[nums.size()];
        for(int i=0; i<s; ++i) dp[i] = 0;
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = nums[0]+nums[2];
        for(int i=3; i<s;++i){
            dp[i] = nums[i]+max(dp[i-2], dp[i-3]);
        }
        return max(dp[s-1], dp[s-2]);
    }
};
