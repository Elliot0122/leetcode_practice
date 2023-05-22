class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans;
        ans.push_back(-1);
        ans.push_back(-1);
        int length = nums.size();
        if(length == 0) return ans;
        int start = -1, end = -1;
        bool notfound = false;
        while(start == -1 || end == -1){
            int head = 0, tail = length-1;
            if(notfound) break;
            while(true){
                if(head == tail && nums[head] != target){
                    notfound = true;
                    break;
                }
                int half = (head + tail+1)/2;
                if(nums[half] > target)
                    tail = half-1;
                else if (nums[half] < target)
                    head = half;
                else{
                    if(start == -1){
                        if(half == 0 || nums[half-1] != target){
                            start = half;
                            break;
                        }else 
                            tail = half-1;
                    }else{
                        if(half == length-1 || nums[half+1] != target){
                            end = half;
                            break;
                        }else
                            head = half;
                    }
                }
            }
        }
        ans[0] = start;
        ans[1] = end;
        return ans;
    }
};
