class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort list
        # go through list one for loop
        # counter each time it is +1

        if len(nums) == 0:
            return 0

        sort_nums = sorted(nums)

        prev = sort_nums[0]
        counter = 1
        count_list = []

        for n in sort_nums:
            if n - prev == 1:
                counter += 1
                prev = n
            elif n - prev == 0:
                prev = n
            else:
                count_list.append(counter)
                counter = 1
                prev = n
        count_list.append(counter)

        return max(count_list)