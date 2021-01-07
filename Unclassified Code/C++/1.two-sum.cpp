// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem1.h"
#include <unordered_map>

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); i++)
        {
            auto item = hashtable.find(target - nums[i]);
            if (item != hashtable.end())
            {
                return {item->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};
// @lc code=end

