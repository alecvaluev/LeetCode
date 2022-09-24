class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        /*for(auto& num: nums){
            num = num * num;
        }
        sort(nums.begin(), nums.end());
        return nums;
        */
        vector<int> squared;
        int n = nums.size(),
            minPos = n - 1,
            left = minPos, right = minPos;
        
        for(int i = 0; i < n; i++){ //O(n)
            if(nums[i] >= 0){
                minPos = i;
                break;
            }
        }
        left = minPos - 1;
        right = minPos;
        while(left >= 0 && right < n){
            
            if(abs(nums[left]) < abs(nums[right])){
                squared.push_back(nums[left] * nums[left]);
                left--;
            }
            else{
                squared.push_back(nums[right] * nums[right]);
                right++;
            }
        }
        while(left >= 0){
            squared.push_back(nums[left] * nums[left]);
                left--;
        }
        while(right < n){
            squared.push_back(nums[right] * nums[right]);
                right++;
        }
        return squared;
    }
};