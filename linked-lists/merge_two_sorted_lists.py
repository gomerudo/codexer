# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None and l2 is None:
            return None
    
        if l1 is None and l2 is not None:
            return l2
        
        if l2 is None and l1 is not None:
            return l1

        
        # Start points to the lowest one
        root = l1 if l1.val < l2.val else l2
        main = root
        other = l2 if l1.val < l2.val else l1
        
        last = root
        while main is not None and other is not None:
            # node = main if main.val < other.val else other
            
            if main.val < other.val:
                last = main
                main = main.next
            else:
                aux = last.next
                last.next = other
                last = other
                main = other.next
                other = aux
        
        if other is not None:
            last.next = other
        return root