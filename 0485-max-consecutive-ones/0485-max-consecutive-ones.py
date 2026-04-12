class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sliding window
        # two pointers
        l = 0
        r = 0
        max_ones = 0
        curr_counter = 0

        while r < len(nums):
            if nums[l] == 1 and nums[r] == 1:
                curr_counter += 1
                r += 1
            elif nums[r] == 0:
                max_ones = max(max_ones, curr_counter)
                curr_counter = 0
                l = r + 1
                r = l
            elif nums[l] == 0:
                l = l + 1
                r = l + 1

        max_ones = max(curr_counter, max_ones)

        return max_ones
        