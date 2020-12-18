// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem665.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=665 lang=cpp
 *
 * [665] Non-decreasing Array
 */

// @lc code=start
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        nums.insert(nums.begin(), -100000);
        nums.push_back(100000);
        int count = 0;
        for (int i = 1; i < nums.size() - 1; i++)
        {
            if (count > 1)
                return false;
            if (nums[i] > nums[i + 1])
            {
                if (nums[i - 1] > nums[i + 1] && nums[i] > nums[i + 2])
                    return false;
                else
                    count += 1;
            }
        }
        return true;
    }
};
// @lc code=end

