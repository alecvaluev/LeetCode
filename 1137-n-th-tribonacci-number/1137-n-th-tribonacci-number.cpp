class Solution {
public:
    int tribonacci(int n) {
        /* solution 1
        
        if(n == 0) return 0;
        if(n < 3) return 1;
        
        vector<int> map(39, 0);
        map[0] = 0;
        map[1] = 1;
        map[2] = 1;
        
        for(int i = 3; i <= n; i++){
            map[i] = map[i - 1] + map[i - 2] + map[n - 3];
        
        }
        return map[n];
        */
        
        int a = 0;
        int b = 1;
        int c = 1;
        
        if(n == 0) return a;
        if(n < 3) return b;
        
        for(int i = 3; i <= n; i++){
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
};