class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        // solution O(n^2)
        /*int rows = accounts.size();
        int cols = accounts[0].size();
        int reachest = 0;
        
        for(int i = 0; i < rows; i++){
            int sum = 0;
            for(int j = 0; j < cols; j++){
                sum += accounts[i][j];        
            }
            reachest = max(sum, reachest);
        }
        return reachest;*/
        
        // less space
        int reachest = 0;
        
        for(auto row: accounts){
            int sum = 0;
            for(auto col: row){
                sum += col;        
            }
            reachest = max(sum, reachest);
        }
        return reachest;
    }
};