# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.isEqual(root.left,root.right)
    def isEqual(self,left_tree,right_tree):
        if (left_tree==None and right_tree==None) or \
                (left_tree!=None and right_tree!=None and left_tree.val==right_tree.val and
                         (self.isEqual(left_tree.left,right_tree.right)&self.isEqual(left_tree.right,right_tree.left))==True):
            return True
        else:
            return False