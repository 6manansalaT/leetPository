class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointers
        # calculate max profit
        l = 0
        r = 0
        max_profit = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                diff = prices[r] - prices[l]
                max_profit = max(diff, max_profit)
                r += 1
            else:
                l = r

        return max_profit
