class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        //time O(n) space O(n)
        /*vector<vector<int>> answer;
        
        int first = newInterval[0],
            last = newInterval[1];
        
        for(int i = 0; i < intervals.size(); i++){
            int start = intervals[i][0],
                end = intervals[i][1];
            // no overlap
            if(end < first){
                answer.push_back(intervals[i]);
            }
            //no overlap
            else if (last < start){
                answer.push_back(newInterval);
                newInterval = intervals[i];
            }
            //overlap in 1 of 4 ways
            else{
                newInterval[0] = min(start, first);
                newInterval[1] = max(end, last);
            }
        }
        //push last interval it could be new or old interval
        answer.push_back(newInterval);
        return answer;*/
        int n = intervals.size()-1;
        vector<vector<int>> res;
        
        for(int i = 0; i < intervals.size(); i++){
            if(intervals[i][1] < newInterval[0]){
                res.push_back(intervals[i]);
            }
            
            else if(intervals[i][0] > newInterval[1]){
                res.push_back(newInterval);
                newInterval = intervals[i];
            }
            
            else if(intervals[i][1] >= newInterval[0] || intervals[i][0] <= newInterval[1]){
                newInterval[0] = min(intervals[i][0], newInterval[0]);
                newInterval[1] = max(intervals[i][1], newInterval[1]);
            }
        }
       res.push_back(newInterval);
       return res;
    }
};