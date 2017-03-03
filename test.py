# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer1=head
        while pointer1.next!=None:
            if pointer1.next.val>=pointer1.val:
                pointer1=pointer1.next
            else:
                break
        if pointer1.next==None:
            return head
        else:
            pointer2 = self.sortList(pointer1.next)
            pointer1.next = None
            pointer1=head
            start=pointer=ListNode(0)
            while pointer1!=None and pointer2!=None:
                if pointer1.val<pointer2.val:
                    pointer.next=pointer1
                    pointer1=pointer1.next
                else:
                    pointer.next=pointer2
                    pointer2=pointer2.next
                pointer=pointer.next
            if pointer1==None:
                pointer.next=pointer2
            else:
                pointer.next=pointer1
            return start.next
a=ListNode(3)
b=ListNode(2)
c=ListNode(5)
d=ListNode(8)
e=ListNode(4)
f=ListNode(6)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
s=Solution()
print s.sortList(a)