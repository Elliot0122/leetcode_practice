class Solution {
public:
    string longestPalindrome(string s) {
        int ttl_length = s.size();
        int ans_len = 1;
        string ans = s.substr(0, 1);
        int length = 0;
        
        if(ttl_length == 1) return s;
        
        for(int i=0; i<ttl_length; ++i){
            length = 0;
            while(i-length>=0 && i+length<ttl_length){
                if(s[i-length] != s[i+length]) break;
                length++;
            }
            length--;
            if(ans_len < length*2+1){
                ans_len = length*2+1;
                ans.assign(s.substr(i-length, length*2+1));
            }
            length = 0;
            while(i-length>=0 && i+length+1<ttl_length){
                if(s[i-length] != s[i+length+1]) break;
                length++;
            }
            if(ans_len < length*2){
                ans_len = length*2;
                ans.assign(s.substr(i-length+1, length*2));
            }
        }
        return ans;
    }
};
