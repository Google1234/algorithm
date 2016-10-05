class Node(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result=""
        start=Node(-1,None)
        b=start
        i=1
        mul=1
        while i<=n:
            a=Node(i,None)
            b.next=a
            b=a
            mul=mul*i
            i+=1


        while n!=0:
            mul=mul/n
            pointer=start
            base_k=0
            while base_k+mul<k:
                pointer=pointer.next
                base_k+=mul
            result+=str(pointer.next.val)
            pointer.next=pointer.next.next
            k-=base_k
            n-=1
        return result