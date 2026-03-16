class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # go through each item
        # sum of item
        # return max

        max_wealth = 0

        for acc in accounts:
            curr_sum = sum(acc)
            max_wealth = max(max_wealth, curr_sum)

        return max_wealth