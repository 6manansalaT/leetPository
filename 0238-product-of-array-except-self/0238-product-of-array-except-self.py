import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # iterate through array once
        # prefix and post fix

        res_arr = [1] * len(nums)
        pref = 1
        post = 1

        for i in range(len(nums)):
            res_arr[i] = pref
            pref *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            res_arr[j] *= post
            post *= nums[j]
        return res_arr