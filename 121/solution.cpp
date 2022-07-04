class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len==1) return 0;
        
        int minprice = prices[0];
        int profit = 0;
        for(int i=0; i<len; ++i){
            minprice = min(minprice, prices[i]);
            profit = max(prices[i]-minprice, profit);
        }
        return profit;
    }
};
