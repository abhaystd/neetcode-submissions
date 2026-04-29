class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>>mp;
        for(int i=0;i<strs.size();i++){
            string s = strs[i];
            sort(s.begin(),s.end());
            mp[s].push_back(strs[i]);
        }
        vector<vector<string>>res;
        for(auto it:mp){
            // auto idxs=it.second;
            // vector<string>temp;
            // for(int i=0;i<idxs.size();i++){
            //     temp.push_back(strs[i]);
            // }
            res.push_back(it.second);
        }
        return res;
    }
};
