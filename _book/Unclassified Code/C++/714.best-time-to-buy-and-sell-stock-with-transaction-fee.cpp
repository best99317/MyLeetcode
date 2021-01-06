// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem714.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode id=714 lang=cpp
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        // Boundary condition
        if (prices.size() == 1)
            return 0;
        int res = 0;
        int buy = 2147483647; // Initialize the buying price to infinity
        for (int i = 0; i < prices.size() - 1; i++)
        {
            if (prices[i] < prices[i + 1] - 2)
            { // When found the turning valley, we buy
                buy = min(prices[i], buy);
            }
            else if (buy != 2147483647)
            {                           // When found the turning peak,
                res += prices[i] - buy; // and we have already bought,
                buy = 2147483647;       // we sell and reset the initial buying price.
            }
        }
        // One special case is that the prices never decrease so that there is no peak
        if (buy != 2147483647)
            res += prices[prices.size() - 1] - buy;
        return res;
    }
};
// @lc code=end

