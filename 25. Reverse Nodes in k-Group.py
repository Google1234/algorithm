# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==1:
            return head

        last2=current=head
        count=1
        begin=last1=before=ListNode(0)
        while current:
            after=current.next
            current.next=before
            before=current
            current=after
            if count%k==0:
                last1.next=before
                last1=last2
                last2=current
            count+=1
        if count%k!=1:
            current=before
            after=None
            count-=1
            while count%k!=1:
                before=current.next
                current.next=after
                after=current
                current=before
                count-=1
            current.next=after
            last1.next=current
        else:
            last1.next=None
        return begin.next