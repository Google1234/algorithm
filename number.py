# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result=[]
        self.DFS(0,root)
        return self.result

    def DFS(self,lever,node):
        if node!=None:
            if lever>=len(self.result):
                self.result.append([])
            self.result[lever].append(node.val)
            self.DFS(lever+1,node.left)
            self.DFS(lever+1,node.right)

