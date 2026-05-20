# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng,i=0,0
        point=head
        while point:
            leng+=1
            point=point.next
        
        rem=leng-n
        
        poi=head
        while i < rem-1:
            i+=1
            poi=poi.next
            
        dummy=ListNode()
        if rem==0 and leng>0:
            head=head.next
        elif poi.next:
            poi.next=poi.next.next
        
        '''else:
            head=None'''

        return head
