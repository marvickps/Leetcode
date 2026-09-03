# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        half = slow.next
        slow.next = None

        prev = None
        curr = half

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        half = prev

        first = head
        temp = first
        head = head.next

        while head and half:
            #slow [3,4]
            #half [5,7,9] 
            #...[2]-[5]
            temp.next = half
            temp = temp.next
            half = half.next

            temp.next = head
            temp = temp.next
            head = head.next

        temp = head or half

        head = first
            
            

            



        
        
