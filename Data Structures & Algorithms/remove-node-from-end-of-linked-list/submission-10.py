# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        lenght = 0

        while dummy:
            lenght += 1
            dummy = dummy.next
            
        print(lenght)
        point = head
        rem_ind = lenght - n
        if rem_ind == 0:
            return head.next

        for i in range(lenght - n - 1):
            point = point.next

        if point.next:
            point.next = point.next.next

        return head