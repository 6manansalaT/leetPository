# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # two pointers s & f
        # s is slow + 1, f is fast + 2
        # while loop
        # when meet, check if it is null
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False