class Solution {
public:
    int hammingWeight(uint32_t n) {
        int mask = 1;
        int ans = 0;
        while(n){
            int temp = mask & n;
            ans+=temp;
            n = n>>1;
        }
        return ans;
    }
};
