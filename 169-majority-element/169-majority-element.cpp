class Solution {
public:
    int majorityElement(vector<int>& nums) {
        //use map to count frequencies O(n)
        //sort -> count the middle and that's the answer
        
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};