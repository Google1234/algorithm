class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer=head
        for i in xrange(n):
            if pointer!=None:
                pointer=pointer.next
            else:
                return None
        if pointer==None:
            return head.next
        before=head
        while pointer.next!=None:
            pointer=pointer.next
            before=before.next
        before.next=before.next.next
        return head