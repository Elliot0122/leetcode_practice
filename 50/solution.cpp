class Solution {
public:
    double myPow(double x, int N) {
        long n = N;
        if(n<0){
            x = 1/x;
            n = -n;
        }
        double ans = 1.0;
        int exp[33] = {0};
        int mask = 1, end = 0;
        for(int i=0; i<33; i++){
            if(n==0){
                end = i;
                break;
            }
            exp[i] = mask&n;
            n = n>>1;
        }
        for(int i=0; i<end; i++){
            if(exp[i] == 1) ans *= x;
            x = x*x;
        }

        return ans;
    }
};
