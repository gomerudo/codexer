"""You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order. Merge all the linked-lists into one sorted linked-list and
return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])
            
        return res