class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> ans;
        int len = nums.size();
        for(int i=0; i<len; ++i){
            if(map.find(target-nums[i]) == map.end()){
                map[nums[i]] = i;
                continue;
            }
            ans.push_back(map[target-nums[i]]);
            ans.push_back(i);
            return ans;       
        }
        return ans;
    }
};
