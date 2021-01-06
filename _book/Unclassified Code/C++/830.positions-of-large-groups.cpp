/*
 * @lc app=leetcode id=830 lang=cpp
 *
 * [830] Positions of Large Groups
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int n = s.size();
        int l = 0, r = 0;
        vector<vector<int>> res;
        for (int i = 0; i < n - 1; i++)
        {
            if (s[i] == s[i + 1])
            {
                l = min(l, i);
                r = max(r, i + 1);
                if (i == n - 2 && r - l + 1 >= 3)
                    res.push_back({l, r});
            }
            else
            {
                if (r - l + 1 >= 3)
                {
                    res.push_back({l, r});
                }
                l = i + 1;
            }
        }
        return res;
    }
};
// @lc code=end

