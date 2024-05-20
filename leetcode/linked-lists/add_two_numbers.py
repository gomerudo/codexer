"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2: 
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addDigits(self, n1, n2, carry):
        res = n1 + n2 + carry
        return res // 10, res % 10

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeA = l1
        nodeB = l2
        c = 0
        
        root = None
        tmp = None

        # We do not stop until all lists are traversed and there's no carry (c)
        # number.
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