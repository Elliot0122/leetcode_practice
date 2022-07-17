class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        
        if(nums[left] == target)
            return left;
        else if(nums[right] == target)
            return right;
        while(right > left+1){
            if(nums[(left+right)/2] == target)
                return (left+right)/2;

            if(nums[(left+right)/2] < nums[right]){
                if(nums[(left+right)/2] < target && target < nums[right])
                    left = (left+right)/2;
                else
                    right = (left+right)/2;
            }else{
                if(nums[left] < target && target < nums[(left+right)/2])
                    right = (left+right)/2;
                else
                    left = (left+right)/2;
            }
        }
        return -1;
    }
};
