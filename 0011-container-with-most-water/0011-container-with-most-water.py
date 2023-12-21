class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_int = 0
        s, e = 0, len(height) - 1
        
        while s < e:
            max_int = max(max_int, (e - s) * min(height[s], height[e]))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
            
        
        return max_int
        