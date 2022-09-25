class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        //brutal force - O(nk) - iterate thrtough vector and expand window until its >= target
        
        //optimized - O(n)
        int winStart = 0,
            n = nums.size(),
            minLength = INT_MAX,
            sum = 0;
        
        for(int winEnd = 0; winEnd < n; winEnd++){
            sum += nums[winEnd];
            
            while(sum >= target){
                minLength = min(minLength, winEnd - winStart + 1);
                sum -= nums[winStart];
                winStart++;
            }
        }
        return (minLength == INT_MAX)? 0 : minLength;
    }
};