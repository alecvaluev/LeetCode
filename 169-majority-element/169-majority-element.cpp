class Solution {
public:
    int majorityElement(vector<int>& nums) {
        //use map to count frequencies O(n) 
        //sort -> count the middle and that's the answer
        
        /*
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
        */
        
        //candidate element O(n)
        int candidate = nums[0],
            count = 1;
        
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == candidate) count++;
            else if (count == 0){
                candidate = nums[i];
                count = 1;
            }
            else count--;
        }
        return candidate;
    }
};