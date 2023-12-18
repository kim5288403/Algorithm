class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2**31
        max_val = 2**31 - 1
        
        result = 0
        y = abs(x)
        
        while y > 0:
            result *= 10
            result += y % 10
            y //= 10
            
        if x < 0:
            result *= -1
        else:
            result *= 1
        
        if min_val <= result <= max_val:
            return result
        else:
            return 0