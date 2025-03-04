class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_cap = 0
        while left < right:
            max_cap = max(max_cap, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_cap
