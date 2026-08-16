class ListNode:
    def __init__(self,val,tail=None):
        self.val = val
        self.tail = tail

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #first lets make a linked list
        head = ListNode(students[0])
        cur = head

        for item in students[1:]:
            cur.tail = ListNode(item)
            cur = cur.tail
        #neow let's do

        def deque():
            nonlocal head
            head = head.tail

        def circle():
            nonlocal head,cur
            cur.tail = head
            cur = cur.tail
            head = head.tail
            cur.tail = None

        k = 0
        i = 0
        while i<len(sandwiches):
            if(head.val==sandwiches[i]):
                deque()
                i+=1
                k = 0
            else:
                k+=1
                if (k==len(students)-i):
                    return len(students)-i    
                circle()
        return 0        
