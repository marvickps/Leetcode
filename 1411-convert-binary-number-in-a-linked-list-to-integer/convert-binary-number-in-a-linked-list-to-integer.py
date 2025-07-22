# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse_linked_list(self, head):
		#head: 1>2>3>4>5
        prev = None
        current = head #1>2>3>4>5
        
        while current:
            next_node = current.next  
            #next_node:  2
            current.next = prev      
            #current.next: none      # 1 -> None
            prev = current          
            #prev: 1 
            current = next_node      
                #current: 2
        return prev 

    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        temp = 0
        i = 0
        head = self.reverse_linked_list(head)

        while head:
            
            temp = temp + head.val * (2 ** i)
            head = head.next
            i=i+1
        return temp
