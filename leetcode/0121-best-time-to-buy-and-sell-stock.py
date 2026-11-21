# Track the minimum price seen so far while scanning left to right;
# at each day, the best profit is the current price minus that minimum.
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p = prices
        mnt = p[0]
        sell = 0
        for i in p:
            if i - mnt > sell:
                sell = i - mnt
            if i < mnt:
                mnt = i
        return sell