class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int start = 0;
        int end = nums.size()-1;
        if(end == 0) return 0;
        if(nums[0] > nums[1]) return 0;
        if(nums[end] > nums[end-1]) return end;

        while(start <= end){
            int mid = start + (end-start)/2;
            if(nums[mid] > nums[mid+1] && nums[mid] > nums[mid-1]) return mid;
            else if(nums[mid] < nums[mid+1]) start = mid+1;
            else if(nums[mid] < nums[mid-1]) end = mid-1;
        }
        return -1;
    }
};
