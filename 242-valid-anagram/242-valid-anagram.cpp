class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        if(n != t.size()) return false;
        
        int map[26] = {0};
        
        for(int i = 0; i < n; i++){
            map[s[i] - 'a']++;
            map[t[i] - 'a']--;
        }
        
        for(auto& count: map){
            if(count != 0) return false;
        }
        
        return true;
    }
};