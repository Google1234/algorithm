class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        left=head
        right=head.next
        begin=last=ListNode(0)
        while True:
            last.next=right
            left.next=right.next
            right.next=left
            last=left
            left=left.next
            if left==None:
                last.next=left
                break
            right=left.next
            if right==None:
                last.next=left
                break
        return begin.next

