class Solution(object):
    def MaxArea(self,height):
        max_area = 0
        left = 0
        right = len(height) -1

        while left < right:
            max_area = max(max_area,(right-left) * min(height[right],height[left]))

            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max_area
    
# ------------test-----------
height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
ans = sol.MaxArea(height)
print(ans)