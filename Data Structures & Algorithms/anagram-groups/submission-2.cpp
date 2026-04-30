class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n=strs.size();
        vector<vector<int>>freq(n,vector<int>(26,0));
        for(int i=0;i<strs.size();i++){
            for (char ch:strs[i]){
                freq[i][ch-'a']++;
            }
        }
        map<vector<int>,vector<int>>mp;
        for (int i=0;i<n;i++){
            mp[freq[i]].push_back(i);
        }
        vector<vector<string>>res;
        for(auto it:mp){
            int m=it.second.size();
            vector<string>temp;
            for(int i=0;i<m;i++){
                temp.push_back(strs[it.second[i]]);
            }
            res.push_back(temp);
        }
        return res;
    }
};
