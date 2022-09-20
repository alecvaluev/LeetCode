class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> mapping;
        set<int>::iterator iter;
        
        for(int i: nums){
            iter = mapping.find(i);
            if(iter != mapping.end()) return true;
            else mapping.insert(i);
        }
        return false;
    }
};