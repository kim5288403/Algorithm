# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(li1, li2):
            dummy = node = ListNode(None)

            while li1 and li2:
                
                if li1.val < li2.val:
                    node.next = li1
                    li1 = li1.next
                else:
                    node.next = li2
                    li2 = li2.next
                node = node.next
                
            node.next = li1 or li2        
            return dummy.next
        
        if len(lists) == 0:
            return None
    
        for i in range(len(lists) - 1):
            lists[i + 1] = mergeTwoList(lists[i], lists[i + 1])
       
    
        return lists[len(lists) - 1]
        
        