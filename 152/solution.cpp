class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ans = nums[0];
        int tmax = 1;
        int tmin = 1;
        for(int i=0; i<nums.size(); ++i){
            int temp = tmax*nums[i];
            tmax = max(temp, max(tmin*nums[i], nums[i]));
            tmin = min(temp, min(tmin*nums[i], nums[i]));
            ans = max(tmax, ans);
        }
        return ans;
    }
};
