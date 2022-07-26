class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp = {nums[0]};

        for(int i=0; i<nums.size(); ++i){
            if(nums[i] > dp.back())
                dp.push_back(nums[i]);
            else
                dp[binarysearch(dp, nums[i])] = nums[i];
        }
        return dp.size();
    }
    int binarysearch(vector<int>& dp, int& target){
        int start = 0, end = dp.size()-1;
        
        while(start < end){
            int mid = (start+end)/2;
            if(dp[mid] < target)
                start = mid+1;
            else
                end = mid;
        }
        return end;
    }
};
