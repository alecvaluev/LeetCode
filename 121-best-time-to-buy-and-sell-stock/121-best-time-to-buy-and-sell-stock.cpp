class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //brute force - calc every possible solution using 2 inner for-loops O(n^2) 
        //optimized - time O(n); - sliding window(Kadane's algo)
        
        /*int n = prices.size(),
            profit = 0,
            dayBuy = 0;
            
        for(int day = 1; day < n; day++){
            while(day < n && prices[dayBuy] < prices[day]){
                profit = max(profit, prices[day] - prices[dayBuy]);
                day++;
            }
            dayBuy = day;
        }
        return profit;*/
        
        //more optimized for space
        int n = prices.size(),
            profit = 0,
            buy = prices[0];
            
        for(int day = 1; day < n; day++){
            if(prices[day] - buy > profit) profit = prices[day] - buy;
            if(prices[day] < buy) buy = prices[day];
        }
        return profit;
    }
};