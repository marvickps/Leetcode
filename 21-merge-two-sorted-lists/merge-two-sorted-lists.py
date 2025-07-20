# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = ListNode()
        final = temp


        while list1 and list2:
            if list1.val < list2.val:
                final.next = list1
                list1 = list1.next

            else:
                final.next  = list2
                list2 = list2.next
            final = final.next

        if list1:
            final.next = list1
        if list2:
            final.next =list2


        return temp.next



        
