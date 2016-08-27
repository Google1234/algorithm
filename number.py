# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return []
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
           Node1=lists[0]
           Node2=lists[1]
           begin=Last=ListNode(0)
           while Node1!=None and Node2!=None:
               if Node1.val>Node2.val:
                   Last.next=Node2
                   Node2=Node2.next
               else:
                   Last.next=Node1
                   Node1=Node1.next
               Last=Last.next
           if Node1!=None:
               Last.next=Node1
           if Node2!=None:
               Last.next=Node2
           return begin.next
        else:
            return self.mergeKLists([self.mergeKLists(lists[:len(lists)/2]),self.mergeKLists(lists[len(lists)/2:])])
