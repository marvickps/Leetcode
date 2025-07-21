# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode()
        final = temp

        while head:
            if final == temp or head.val != final.val:
                final.next = head # 3-0, 3 = 3-3 = 
                final = final.next
            head = head.next
            final.next = None
        return temp.next
     