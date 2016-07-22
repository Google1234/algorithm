
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        last=ListNode(0)
        result=last
        while l1!=None and l2!=None:
            sum=l1.val+l2.val+c
            pointer=ListNode(sum%10)
            c=sum/10
            last.next=pointer
            last=pointer
            l1=l1.next
            l2=l2.next
        if l1==None:
            while l2!=None:
                sum=l2.val+c
                pointer=ListNode(sum%10)
                c=sum/10
                last.next=pointer
                last=pointer
                l2=l2.next
        if l2 == None:
            while l1 != None:
                sum = l1.val + c
                pointer = ListNode(sum % 10)
                c = sum / 10
                last.next = pointer
                last = pointer
                l1 = l1.next
        if c!=0:
            pointer=ListNode(c)
            last.next=pointer
        return result.next