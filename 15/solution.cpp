class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        set<vector<int>> temp;
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<nums.size(); ++i){
            if(nums[i] > 0)break;
            if(i>0 && nums[i] == nums[i-1])continue;
            int target = -nums[i];
            unordered_map<int, int> map;
            for(int j=i+1; j<nums.size(); j++){
                if(map.find(target-nums[j]) == map.end())
                    map[nums[j]] = j;
                else{
                    vector<int> vec{nums[i], nums[map[target-nums[j]]], nums[j]};
                    temp.insert(vec);
                }
            }
        }
        for(auto a:temp)
            ans.push_back(a);
        return ans;
    }
};
