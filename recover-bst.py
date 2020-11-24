# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
numbers = []
class Solution:
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def traverse(root):
            global numbers
            if root.left:
                traverse(root.left)
            numbers.append(root.val)
            if root.right:
                traverse(root.right)
        
        global numbers
        numbers = []
        traverse(root)
        x = []
        numbers2 = sorted(numbers)
        for i in range(len(numbers2)):
            if numbers2[i]!=numbers[i]:
                x+=[numbers[i]]
        def traverse1(root, x):
            if root.left:
                traverse1(root.left, x)
            if root.val==x[0]:
                root.val = x[1]
            elif root.val == x[1]:
                root.val = x[0]
            if root.right:
                traverse1(root.right, x)
        
        traverse1(root, x)
        return root
