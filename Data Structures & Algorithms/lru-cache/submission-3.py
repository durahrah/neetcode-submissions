class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # head least, tail most

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node): # (Minor: lowercase 'node' is preferred to avoid shadowing the class name)
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.next, node.prev = None, None

    def insert(self, key, val):
        prev = self.tail.prev
        node = Node(key, val)
        prev.next = node
        node.prev, node.next = prev, self.tail
        self.tail.prev = node
        return node

    def get(self, key: int) -> int:
        # hash map to get O(1) lookup
        if key in self.cache:
            self.remove(self.cache[key])
            node = self.insert(key, self.cache[key].val)
            self.cache[key] = node #repointing the node
            return node.val
        else:
            return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = self.insert(key, value)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            del self.cache[self.head.next.key] # deleted lru from cache
            self.remove(self.head.next)