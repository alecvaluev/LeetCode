class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //brute force time O(n); - sliding window
        
        int n = prices.size(),
            profit = 0,
            dayBuy = 0;
            
        for(int day = 1; day < n; day++){
            while(day < n && prices[dayBuy] < prices[day]){
                profit = max(profit, prices[day] - prices[dayBuy]);
                day++;
            }
            dayBuy = day;
        }
        return profit;
    }
};