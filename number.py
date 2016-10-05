# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None
        len=1
        pointer=head
        while pointer.next!=None:
            pointer=pointer.next
            len+=1
        pointer.next=head
        k=k%len
        k=len-k
        pointer=head
        t=1
        while t<k:
            t+=1
            pointer=pointer.next
        result=pointer.next
        pointer.next=None
        return result
