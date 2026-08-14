class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

        #basically blueprint of a node
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        #THESE are the dummy nodes ! they point to eo
        

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index>0:
            cur = cur.next
            index= index -1
        if cur and cur!=self.tail and index==0:
            return cur.val
        else:
            return -1        
        

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        node = ListNode(val)
        node.prev=self.head
        node.next=cur
        self.head.next = node
        cur.prev = node
        

    def addAtTail(self, val: int) -> None:
        cur = self.tail.prev
        node = ListNode(val)
        node.next=self.tail
        node.prev = cur
        cur.next = node
        self.tail.prev = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        cur = self.head.next
        while cur and index>0:
            cur=cur.next
            index=index-1
        if cur and index==0:
            prev = cur.prev
            node.next = cur
            node.prev = prev
            prev.next = node
            cur.prev = node

        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if cur and cur!=self.tail and index==0:
            prev,next = cur.prev,cur.next
            prev.next = next
            next.prev = prev
          

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)