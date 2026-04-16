class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # make nums a sorted set
        # count how many nums is before certain number
        
        res_list = []
        sort_nums = sorted(nums)

        for n in nums:
            res_list.append(len(sort_nums[0:sort_nums.index(n)]))

        return res_list