class Solution(object):
    def FindDuplicateElement(nums):
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        result = nums[0]

        while result != slow:
            slow=nums[slow]
            result = nums[result]

        return slow
    

# -----test------


arr = [1,3,4,3,2] 
sol = Solution
print(sol.FindDuplicateElement(arr))