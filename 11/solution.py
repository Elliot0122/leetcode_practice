class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        heightLen = len(height)-1
        left = 0
        right = heightLen
        width = heightLen
        max_vol = 0
        
        for i in range(heightLen):
            max_vol = max(max_vol, width*min(height[left], height[right]))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            width-=1
        return max_vol
            
        

