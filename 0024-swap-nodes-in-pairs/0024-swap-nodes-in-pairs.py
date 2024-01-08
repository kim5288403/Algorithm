# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        dummy.next = head
        c = dummy

        while c.next and c.next.next:
            f = c.next
            s = c.next.next
            
            c.next = s
            f.next = s.next
            s.next = f
            
            c = c.next.next
        
        return dummy.next
            
            
        
        