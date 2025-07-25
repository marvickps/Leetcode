# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #1-2-3-4-5
        #5-4-3-2-1


        temp2 = None
        while head:
            next = head.next #2-3-4-5 #3-4-5 #4-5 #5
            head.next = temp2 #1
            temp2 = head #1
            head = next
        return temp2


            

        