class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None :
            return l2
        if l2==None:
            return l1
        pointer1=l1
        pointer2=l2
        begin=last=ListNode(0)
        while pointer1!=None and pointer2!=None:
            if pointer1.val>pointer2.val:
                last.next=pointer2
                pointer2=pointer2.next
            else:
                last.next=pointer1
                pointer1=pointer1.next
            last=last.next
        while pointer1!=None:
            last.next=pointer1
            last=last.next
            pointer1=pointer1.next
        while pointer2 != None:
            last.next = pointer2
            last=last.next
            pointer2 = pointer2.next
        return begin.next