class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self,head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left = 0
        right = len(arr)-1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left +=1
            right -=1

        return True
    

# ---------------test-----------------


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)


a.next = b
b.next = c
c.next = d

sol = Solution()
ans = sol.isPalindrome(a)
print(ans)