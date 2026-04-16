class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sort existing list as a set
        # make other set with all numbers
        # subtract sets

        sort_nums = set(nums)
        complete_nums = set(range(1, len(nums) + 1))

        return list(complete_nums - sort_nums)