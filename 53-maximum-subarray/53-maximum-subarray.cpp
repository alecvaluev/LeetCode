class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = INT_MIN,
            currSum = 0;
        
        for(auto i: nums){
            currSum += i;
            
            maxSub = max(maxSub, currSum);
            if(currSum < 0) currSum = 0;
        }
        return maxSub;
    }
};