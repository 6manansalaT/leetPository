class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # left & right boundary
        # bottom & top boundary
        # while l < r
        # have a temp variable and only make one
        # rotate four times??
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t = l
                b = r

                temp = matrix[l][t + i]

                matrix[l][t + i] = matrix[b - i][l]

                matrix[b - i][l] = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = temp
            
            l += 1
            r -= 1

                