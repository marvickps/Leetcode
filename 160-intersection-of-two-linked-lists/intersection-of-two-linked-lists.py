# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp = headA
        temp2 = headB
        
        while temp is not temp2:
            if temp:
                temp = temp.next
            else:
                temp = headB
            
            if temp2:
                temp2 = temp2.next
            else:
                temp2 = headA
            
        return temp

        