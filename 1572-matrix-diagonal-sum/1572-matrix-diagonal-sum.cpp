class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        // O(n) time, O(1) space
        int n = mat.size(),
            sum = 0;
        //primary
        for(int i = 0, j = n - 1; i < n; i++, j--){
            sum += mat[i][i];
            if(i != j) sum += mat[i][j];
        }
        return sum;
    }
};