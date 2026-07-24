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
        
        copy = {}
        

        if head:
            val = Node(head.val)
        else:
            return

        ran_node = node = mapp = head 
        Final = D = dup_list = val
            
        node = node.next
        while node:
            val.next = Node(node.val)
            val = val.next
            node = node.next
            
        while mapp:
            copy[mapp] = dup_list
            mapp = mapp.next
            dup_list = dup_list.next

        while ran_node:
            if ran_node.random:
                D.random = copy[ran_node.random]
            else:
                D.random = None

            ran_node = ran_node.next
            D = D.next

        return Final
