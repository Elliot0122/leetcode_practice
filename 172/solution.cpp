class Solution {
public:
    int trailingZeroes(int n) {
        int cnt = 0;
        int fives = 5;
        while(n/fives){
            cnt += n/fives;
            fives*=5;
        }
        return cnt;
    }
};
