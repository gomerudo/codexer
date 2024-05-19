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
        
        stackA = []
        stackB = []
        
        node = l1
        # Iterate over list 1
        while node is not None:
            stackA.append(node.val)
            node = node.next
            
        node = l2
        # Iterate over list 2
        while node is not None:
            stackB.append(node.val)
            node = node.next
            

        # root = None
        last = None
        
        c = 0
        while stackA or stackB or c > 0:
            a = 0 if not stackA else stackA.pop()
            b = 0 if not stackB else stackB.pop()
            c, s = self.addDigits(a, b, c)
                
            if last is None:
                last = ListNode(s)
                root = last
            else:
                aux = ListNode(s)
                aux.next = last
                last = aux        
        return last
