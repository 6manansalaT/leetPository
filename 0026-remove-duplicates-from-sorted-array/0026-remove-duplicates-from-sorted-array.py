class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers l & r
        # when l and r are the same remove element at r increment r
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
            else: 
                l += 1
                r += 1
        
        return len(nums)