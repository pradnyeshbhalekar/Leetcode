class LinkedList(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self,head):
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        else:
            return None
            
        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
    


# ----- test -----

a = LinkedList(5)
b = LinkedList(10)
c = LinkedList(15)


a.next = b
b.next = c
c.next = b

sol = Solution()
cycle_node = sol.detectCycle(a)

if cycle_node:
    print(cycle_node.val)
else:
    print("-1")
