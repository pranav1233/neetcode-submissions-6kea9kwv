"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mapp={}
        if head:
            val=Node(head.val)
        else:
            return 
        final=copy=val
        start_val=val
        tmp=head.next

        while tmp: 
            val.next=Node(tmp.val)
            val=val.next
            tmp=tmp.next

        tom=head
        while tom:
            mapp[tom]=start_val
            tom=tom.next
            start_val=start_val.next

        while copy:
            if head.random:
                copy.random=mapp[head.random]
            else:
                copy.random = None
            copy=copy.next
            head=head.next

        return final

        

            
