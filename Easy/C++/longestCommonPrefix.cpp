class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        string ans = "";
        sort(strs.begin(),strs.end());
        int lengthStrs = strs.size();
        string firstStr = strs[0];
        string lastStr = strs[lengthStrs - 1];

        for (int i = 0; i < min(firstStr.size(), lastStr.size()); i++) 
        {
            if(firstStr[i] != lastStr[i])
            {
                return ans;
            }
            ans += firstStr[i];
        }
        return ans;

    }
};
