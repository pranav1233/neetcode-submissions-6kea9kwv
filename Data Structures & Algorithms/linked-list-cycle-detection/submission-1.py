# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        li=[]

        while head:
            
            if head: 
                if head in li:
                    return True
                else:
                    li.append(head)
                head=head.next

            '''else: 
                return False'''

        return False
            