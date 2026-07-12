# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head 
        dummy = head
        l1 = ListNode()
        l2 = ListNode()
        
        while fast and fast.next:
            l1.next = slow
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        prev = None
        next = None

        while l2:
            next = l2.next
            l2.next = prev
            prev = l2
            l2 = next

        res = ListNode()

        while head and prev:
            res.next = head
            head = head.next
            res = res.next
            res.next = prev
            prev = prev.next
            res = res.next

        if head:
            res.next=head
        elif prev:
            res.next=prev

        