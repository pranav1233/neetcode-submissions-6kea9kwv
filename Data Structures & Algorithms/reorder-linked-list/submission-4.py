# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        l2 = slow.next
        slow.next = None 

        prev = None
        while l2:
            next = l2.next
            l2.next = prev
            prev = l2
            l2 = next

        l1, l2 = head, prev

        res = ListNode()
        while l1 and l2:
            res.next = l1
            l1 = l1.next
            res = res.next
            res.next = l2
            l2 = l2.next
            res = res.next

        if l1:
            res.next = l1
        elif l2:
            res.next = l2