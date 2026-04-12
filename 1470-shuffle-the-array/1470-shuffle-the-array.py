class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # split arr at n
        # two pointers?
        # create one new array

        p1 = 0
        p2 = n
        ans = []

        while p1 < n and p2 < len(nums):
            ans.append(nums[p1])
            ans.append(nums[p2])

            p1 += 1
            p2 += 1

        return ans