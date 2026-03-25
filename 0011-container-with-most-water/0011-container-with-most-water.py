class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # have a max area variable
        # l and r pointers?
        # l pointer is all the way left
        # right pointer is all the way right
        # move pointer when it is small

        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            this_area = (r - l) * min(height[r], height[l])
            max_area = max(this_area, max_area)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
            
        return max_area
        