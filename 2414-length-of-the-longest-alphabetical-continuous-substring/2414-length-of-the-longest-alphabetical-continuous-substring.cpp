class Solution {
public:
    int longestContinuousSubstring(string s) {
        int longest = 1, curr = 1;
        
        for(int i = 0; i < s.length() - 1; i++){
            if(s.at(i) + 1 == s.at(i + 1)) {
                curr++;
                longest = max(curr, longest);
            }
            else curr = 1;
        }
        return longest;
    }
};