class LinkedList(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def RemoveNodeFromEnd(self,head,n):
        res = LinkedList(0,head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        

        return res.next
    



# ---------------- test---------------

a = LinkedList(5)
b = LinkedList(10)
c = LinkedList(15)
d = LinkedList(20)
e = LinkedList(25)

a.next = b
b.next = c
c.next = d
d.next = e

n = 2

sol = Solution()

finallist = sol.RemoveNodeFromEnd(a,n)


while finallist:
    print(finallist.val, end=" -> " if finallist.next else "\n")
    finallist = finallist.next