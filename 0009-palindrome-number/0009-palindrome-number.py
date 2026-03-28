class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_int = str(x)

        if string_int == string_int[::-1]:
            return True
        else:
            return False