# Definition for a binary tree node.

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        else:
            buff=[[root],[]]
            cur_use=0
            cur_not_use=1-cur_use
            cur_position=[0,0]
            buff_len=[1,0]
            buff_use_len=[1,0]
            result=[[]]
            deepth=0
        while True:
            node=buff[cur_use][cur_position[cur_use]]
            result[deepth].append(node.val)
            if node.left!=None:
                if cur_position[cur_not_use]==buff_len[cur_not_use]:
                    buff[cur_not_use].append(node.left)
                    buff_len[cur_not_use] += 1
                else:
                    buff[cur_not_use][cur_position[cur_not_use]]=node.left
                cur_position[cur_not_use]+=1
                buff_use_len[cur_not_use]+=1
            if node.right!=None:
                if cur_position[cur_not_use]==buff_len[cur_not_use]:
                    buff[cur_not_use].append(node.right)
                    buff_len[cur_not_use]+=1
                else:
                    buff[cur_not_use][cur_position[cur_not_use]] = node.right
                cur_position[cur_not_use] += 1
                buff_use_len[cur_not_use] += 1
            cur_position[cur_use]+=1
            if cur_position[cur_use]==buff_use_len[cur_use]:
                if buff_use_len[cur_not_use]==0:
                    break
                cur_position[cur_use]=0
                cur_position[1-cur_use]=0
                buff_use_len[cur_use]=0
                cur_not_use=cur_use
                cur_use=1-cur_use
                result.append([])
                deepth+=1
        result.reverse()
        return result
