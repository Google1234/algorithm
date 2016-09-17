class quene(object):
    def __init__(self,node,next=None):
        self.val=node
        self.next=next

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        tail=head=quene(root)
        quene_size = 1
        result=[]
        while head!=None:
            size=quene_size
            quene_size=0
            sub_list=[]
            for i in xrange(size):
                if head.val.left!=None:
                    tail.next=quene(head.val.left)
                    tail=tail.next
                    quene_size+=1
                if head.val.right!=None:
                    tail.next=quene(head.val.right)
                    tail=tail.next
                    quene_size+=1
                sub_list.append(head.val.val)
                head=head.next
            result.append(sub_list)
        return result