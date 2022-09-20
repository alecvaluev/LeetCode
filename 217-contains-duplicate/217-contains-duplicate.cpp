class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> mapping;
        
        for(int i: nums){
            if(mapping.count(i) != 0) return true;
            mapping.insert(i);
        }
        return false;
    }
};