class Node:
    def __init__(self,key,value):
        self.next=Node
        self.prev=Node
        self.key=key
        self.value=value

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.cache={}
        
    def insert(self,node):
        prev=self.right.prev
        next=self.right

        node.prev=prev
        node.next=next

        self.right.prev=node
        prev.next=node

    def remove(self,node):
        prev=node.prev
        nxt=node.next

        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node=Node(key,value)
        self.cache[key]=node

        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]
            
        
