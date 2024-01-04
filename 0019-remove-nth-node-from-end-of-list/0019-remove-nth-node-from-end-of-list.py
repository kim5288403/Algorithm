# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        queue = deque()
        dummy = ListNode(None, head)
        node = dummy
        
        for _ in range(n + 1):
            queue.append(node)
            node = node.next
        
        while node:
            queue.popleft()
            queue.append(node)
            node = node.next
        
        queue[0].next = queue[0].next.next
        return dummy.next

        