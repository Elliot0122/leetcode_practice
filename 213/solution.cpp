class Solution {
public:
    int rob(vector<int>& nums) {
        int s = nums.size();
        if(s == 1) return nums[0];
        else if(s==2) return max(nums[0], nums[1]);
        else if(s==3) return max(nums[0], max(nums[1], nums[2]));
        int dp1[s-1], dp2[s];
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        dp2[1] = nums[1];
        dp2[2] = max(nums[1], nums[2]);
        for(int i=2; i<s-1; ++i){
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i]);
        }
        for(int i=3; i<s; ++i){
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i]);
        }
        return max(dp1[s-2], dp2[s-1]);
    }
};
