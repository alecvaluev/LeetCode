class Solution {
public:
    bool isPalindrome(string s) {
        //O(n) time O(1) space
        vector<char> newS;
        
        for(auto& c: s){
            if(isalnum(c)) newS.push_back(tolower(c));
        }
        for(int i = 0, j = newS.size() - 1; i < j; i++, j--){
            if(newS[i] != newS[j]) return false;
        }
        return true;
    }
};