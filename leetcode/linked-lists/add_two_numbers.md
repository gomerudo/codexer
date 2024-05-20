# Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![image](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

>**Input:** `l1 = [2,4,3], l2 = [5,6,4]`<br>**Output:** `[7,0,8]`<br>**Explanation:** `342 + 465 = 807`.

**Example 2:**

>**Input:** `l1 = [0], l2 = [0]`<br>**Output:** `[0]`

**Example 3:**

>**Input:** `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`<br>**Output:** `[8,9,9,9,0,0,0,1]`
 

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

# Solution

## Intuition

The sum of two digits can cause a carriage. This means that the problem is
actually summing up thre digits. We need a function that performs such operation
and returns the carriage. Once that function is written, we simply traverse both
lists and sum.

## Approach

1. Write a function that sums three numbers and returns a tuple of the form `(sum, carriage)`
2. Initialize `carriage = 0`.
3. Initialize pointers `p1 = l1`, `p2 = l2` to traverse the nodes of both lists.
4. Initialize resulting list `result` as `None`.
5. Iterate while either `p1` or `p2` have remaining nodes or there's a carriage to sum.
   1. If `p1` doesn't have another node, make `digit1 = 0`, else makes it `p1.value`
   2. If `p2` doesn't have another node, make `digit2 = 0`, else makes it `p2.value`
   3. Sum the digits and the carriage. This will return a new carriage.
   4. Move pointers to the next node.
   5. Add new node to `result` with the resulting sum.

## Complexity
- Time complexity: `O(max(l1.length, l2.length))`
- Space complexity: `O(max(l1.length, l2.length))`

## Code
```python
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
        
        # These two variables store the result of our sum. `root` is used to
        # return the resulting list. `tmp` is used to link new nodes.
        root = None
        tmp = None
        
        # Iterate while there's something to sum
        while nodeA != None or nodeB != None or c > 0:
            a = 0 if nodeA is None else nodeA.val
            b = 0 if nodeB is None else nodeB.val
            c, s = self.addDigits(a, b, c)
            
            #  Move pointers to the next nodes
            nodeA = None if nodeA is None else nodeA.next
            nodeB = None if nodeB is None else nodeB.next
    
            # Add new node
            if root is None:
                root = ListNode(s)
                tmp = root
            else:
                tmp.next = ListNode(s)
                tmp = tmp.next
        
        return root
```