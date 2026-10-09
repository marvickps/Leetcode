# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        counter = 0 # second priority

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter+=1
        
        dummy = ListNode(0)
        current = dummy

        while heap:
            val, c, node = heapq.heappop(heap)

            current.next = node #dummy->1->
            current = current.next #1->
            if node.next:
                counter+=1
                heapq.heappush(heap,(node.next.val, counter, node.next))
        return dummy.next
    
                