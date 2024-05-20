# Problem

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![image](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

>**Input:** `root = [2,1,3]`<br>**Output:** `true`

**Example 2:**

![image](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

>**Input:** `root = [5,1,4,null,null,3,6]`<br>**Output:** `false`<br>**Explanation:** The root node's value is 5 but its right child's value is 4.

# Intuition
The idea is to perform a left-traversal of the three. If the three is a BTS, the
order will be guaranteed as we traverse.

# Approach
To make this code generic, we perform a full left-traversal and store the result
in an array. Finally we validate the order of the sequence.

We note that a more optimial solution exists if we validate conditions as we traverse.
However, we leave this as a template for other problems that may need left-traversal.

# Complexity
- Time complexity: `O(n)`
- Space complexity: `O(n)` (with improvement this would be 0)

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Left-traversal
    def traverse(self, tree, sequence):
        if tree is None:
            return

        self.traverse(tree.left, sequence)
        sequence.append(tree.val)
        self.traverse(tree.right, sequence)

    def isValidBST(self, root: TreeNode) -> bool:
        sequence = []
        self.traverse(root, sequence)

        # Validate sequence
        i = 1
        while i < len(sequence):
            if sequence[i] <= sequence[i-1]:
                return False
            i += 1
        return True
```
