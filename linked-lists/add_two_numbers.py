# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addDigits(self, a, b, c):
        res = a + b + c
        return res // 10, res % 10

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeA = l1
        nodeB = l2
        c = 0
        
        root = None
        tmp = None
        while nodeA != None or nodeB != None or c > 0:
            a = 0 if nodeA is None else nodeA.val
            b = 0 if nodeB is None else nodeB.val
            c, s = self.addDigits(a, b, c)
            
            nodeA = None if nodeA is None else nodeA.next
            nodeB = None if nodeB is None else nodeB.next
    
            if root is None:
                root = ListNode(s)
                tmp = root
            else:
                tmp.next = ListNode(s)
                tmp = tmp.next
        
        return root