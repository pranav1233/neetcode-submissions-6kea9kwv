# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point = head
        cycle = set()

        while point:
            if point in cycle:
                return True
            
            cycle.add(point)
            point = point.next

        return False