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
        temp = []
        temp2= []
        temp3= ListNode()
        tail = temp3

        
        while list1:
            temp.append(list1.val)
            list1 = list1.next

        while list2:
            temp2.append(list2.val)
            list2 = list2.next

        listFinal = sorted(temp+temp2)

        print(listFinal)

        for num in listFinal:
            tail.next = ListNode(num)
            tail = tail.next
        
        return temp3.next