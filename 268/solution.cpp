class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len = nums.size();
        int sum = 0;
        for(auto i:nums)
            sum+=i;
        return len*(len+1)/2 - sum;
    }
};
