class Solution:
    def trap(self, height: List[int]) -> int:
        water = height.copy()

        for i in range(1, len(water)):
            if water[i] < water[i-1]:
                water[i] = water[i-1]
        highest = 0
        for i in range(len(water)-1, -1, -1):
            if height[i] > highest:
                highest = height[i]
            if water[i] > highest:
                water[i] = highest
        
        return sum(water)-sum(height)
