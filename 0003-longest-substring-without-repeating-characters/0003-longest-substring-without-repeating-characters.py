class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # one loop through whole string
        # use set for characters
        # save the longest length?
        # l and r pointer
        # r goes through list, l increases once there is a duplicate?
        max_len = 0
        char_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                # keep removing l until duplicate is taken out
                char_set.remove(s[l])
                l += 1
            
            # add uniques in
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
