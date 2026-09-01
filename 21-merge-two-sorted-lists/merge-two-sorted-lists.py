# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        firstPointer = result
        
        while list1 and list2:
            if list1.val<list2.val: 
                result.next = list1 #result -> 1-1-2-4
                list1 = list1.next #list1 -> 2-4
            else:
                result.next = list2 #result -> none-1-3-4
                list2 = list2.next #3-4
            
            result = result.next #1-3-4 #
        if list1:
            result.next = list1
        if list2:
            result.next = list2             
        return firstPointer.next