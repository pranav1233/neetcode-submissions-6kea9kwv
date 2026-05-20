# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow= head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        fast=slow.next
        slow.next=None
        
        prev=None 

        while fast:
            next=fast.next
            fast.next=prev
            prev=fast
            fast=next

        l1,l2=head,prev

        while l2:
            n1 = l1.next
            n2=l2.next

            l1.next=l2
            l2.next=n1

            l1=n1
            l2=n2