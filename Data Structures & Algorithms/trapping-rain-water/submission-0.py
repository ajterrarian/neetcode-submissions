class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        start = 0
        end = len(height) - 1
        max_left = height[start]
        max_right = height[end]
        water = 0

        while start <= end:
            if max_left < max_right:
                if height[start] > max_left:
                    max_left = height[start]
                else:
                    water += max_left - height[start]
                start += 1
            else:
                if height[end] > max_right:
                    max_right = height[end]
                else:
                    water += max_right - height[end]
                end -= 1
        return water

        