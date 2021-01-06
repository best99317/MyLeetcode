// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem88.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n){
        int p1 = m - 1;
        int p2 = n - 1;
        if (m == 0)
        {
            nums1 = nums2;
        }
        while (p1 >= 0 && p2 >= 0)
        {
            if (nums1[p1] >= nums2[p2])
            {
                nums1[p1 + p2 + 1] = nums1[p1];
                p1 -= 1;
            }
            else
            {
                nums1[p1 + p2 + 1] = nums2[p2];
                p2 -= 1;
            }
        }
        while (p2 >= 0)
        {
            nums1[p1 + p2 + 1] = nums2[p2];
            p2 -= 1;
        }
    }
};
// @lc code=end

