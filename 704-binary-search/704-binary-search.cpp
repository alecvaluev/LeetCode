class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right){
            int middle = (right + left) / 2;
            
            if(nums[middle] == target) return middle;
            else if(target < nums[middle]){
                right = middle - 1;
            }
            else {
                left = middle + 1;
            }
        }
        return -1;
    }
};