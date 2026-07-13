# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        li = head
        leng=0

        while li:
            leng+=1
            li=li.next

        point=head
        remove_ind=leng-n

        if remove_ind ==0:
            return head.next

        for i in range(remove_ind-1):
            point=point.next

        if point.next:
            point.next=point.next.next

        return head

        



