# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(None)
        result.next = ListNode(None)
        a = result

        while head:
            if head.next == None and head != None:
                a.next.next = ListNode(head.val)
                break
                
            temp = ListNode(head.next.val)
            temp.next = ListNode(head.val)
            a.next.next = temp
            a = temp
            head = head.next.next
        
        return result.next.next
            
            
        
        