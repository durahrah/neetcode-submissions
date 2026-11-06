class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    #head least, tail most

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,Node):
        prev,next = Node.prev,Node.next
        prev.next = next
        next.prev = prev
        Node.next,Node.prev= None,None

    def insert(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev,node.next = prev,self.tail
        self.tail.prev = node
    

    def get(self, key: int) -> int:
        #hash map to get O(1) lookup
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node
        #gta LRU
        if len(self.cache)>self.cap:
            del self.cache[self.head.next.key] #deleted lru from cache
            self.remove(self.head.next) 
    
            
        
