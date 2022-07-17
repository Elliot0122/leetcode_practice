class Solution {
public:
    int findMin(vector<int>& nums) {
        int len = nums.size();
        int left = 0;
        int right = len-1;
        while(right>left+1){
            if(nums[(left+right)/2] > nums[right])
                left = (left+right)/2;
            else
                right = (left+right)/2;
        }
        return min(nums[left], nums[right]);
    }
};
