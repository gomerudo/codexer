# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, tree, sequence):
        
        if tree is None:
            return
        # if tree.left is not None:
        self.traverse(tree.left, sequence)
        sequence.append(tree.val)
        self.traverse(tree.right, sequence)
        
    def isValidBST(self, root: TreeNode) -> bool:
        sequence = []
        self.traverse(root, sequence)
        # Validate sequence
        last = sequence[0]
        i = 1
        while i < len(sequence):
            if sequence[i] <= last:
                return False
            last = sequence[i]
            i += 1
        return True