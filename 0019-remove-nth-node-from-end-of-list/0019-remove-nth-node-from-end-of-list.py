# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # save all nodes in new list??
        # find second to last node
        # get node before that and connect it??
        all_nodes = []
        ptr = head

        while ptr:
            all_nodes.append(ptr)
            ptr = ptr.next
        
        if n == 1 and len(all_nodes) == 1:
            head = None
        elif n == 1:
            all_nodes[-n - 1].next = None
        elif all_nodes[-n] == all_nodes[0]:
            head = all_nodes[-n + 1]
        else:
            all_nodes[-n - 1].next = all_nodes[-n + 1]

        return head