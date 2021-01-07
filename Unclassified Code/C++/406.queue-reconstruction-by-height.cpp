// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem406.h"
#include <algorithm>

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=406 lang=cpp
 *
 * [406] Queue Reconstruction by Height
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>> &people){
        sort(people.begin(), people.end(), [](const vector<int> &u, const vector<int> &v) {
            return u[0] < v[0] || (u[0] == v[0] && u[1] > v[1]);
        });
        int n = people.size();
        vector<vector<int>> ans(n);
        for (const vector<int> &person : people)
        {
            int spaces = person[1] + 1;
            for (int i = 0; i < n; ++i)
            {
                if (ans[i].empty())
                {
                    --spaces;
                    if (!spaces)
                    {
                        ans[i] = person;
                        break;
                    }
                }
            }
        }
        return ans;

    }
};
// @lc code=end

