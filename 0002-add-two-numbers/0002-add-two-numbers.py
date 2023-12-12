# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        listA = l1
        listB = l2
        
        strA = ""
        strB = ""
        
        
        while listA is not None:
            strA = strA + str(listA.val)
            listA = listA.next
            
        while listB is not None:
            strB = strB + str(listB.val)
            listB = listB.next
            
        sum = int(strA[::-1]) + int(strB[::-1])
            
        listNode = None
        for char in str(sum):
            listNode = ListNode(int(char), listNode)
            
        return listNode