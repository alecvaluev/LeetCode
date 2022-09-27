class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        //time O(n)
        int n = nums.size();
        for(int i = 0, j = 1; j < n; j++){
            if(nums[i] == 0 && nums[j] != 0) {
                swap(nums[i], nums[j]);
                i++;
            }
            else if(nums[i] != 0 && nums[i] != 0) i++;
        }
    }
};