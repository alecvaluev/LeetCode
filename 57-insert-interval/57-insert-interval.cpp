class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        //time O(n) space O(n)
        vector<vector<int>> answer;
        
        int& first = newInterval[0],
           & last = newInterval[1];
        
        for(auto& interval: intervals){
            int start = interval[0],
                end = interval[1];
            
            // no overlap
            if(end < first){
                answer.push_back(interval);
            }
            //no overlap
            else if (last < start){
                answer.push_back(newInterval);
                newInterval = interval;
            }
            //overlap in 1 of 4 ways
            else if(interval[1] >= newInterval[0] || interval[0] <= newInterval[1]){
                first = min(start, first);
                last = max(end, last);
            }
        }
        //push last interval it could be new or old interval
        answer.push_back(newInterval);
        return answer;
    }
};