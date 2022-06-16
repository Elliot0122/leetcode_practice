class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> umap;
        vector<vector<string>> ans;
        int cnt = 0;
        for(string s : strs){
            string original = s;
            sort(s.begin(), s.end());
            if(umap.find(s) == umap.end()){
                vector<string> newvec({original});
                umap[s] = cnt;
                ans.push_back(newvec);
                cnt++;
            }else{
                ans[umap[s]].push_back(original);
            }
        }
        return ans;
    }
};
