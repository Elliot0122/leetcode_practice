class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int stringSize = s.size()+1;
        bool dp[stringSize];
        for(int i=0; i<stringSize; ++i) dp[i] = false;
        dp[0] = true;
        int minimum = wordDict[0].size();
        int maximum = wordDict[0].size();
        for(auto word:wordDict){
            int s = word.size();
            minimum = min(minimum, s);
            maximum = max(maximum, s);
        }
        for(int i = minimum; i<stringSize; ++i){
            for(int j = minimum; j<=maximum; ++j){
                if(i-j >= 0){
                    bool temp;
                    if(find(wordDict.begin(), wordDict.end(), s.substr(i-j, j)) != wordDict.end())
                        temp = true;
                    else
                        temp = false;
                    dp[i] = dp[i] || (dp[i-j] && temp);
                }
            }
        }
        return dp[stringSize-1];
    }
};
