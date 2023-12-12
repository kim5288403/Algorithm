class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      
        maxA, maxB = 0, 0
        
        for number in nums:
            
            if number > maxA:
                
                maxA, maxB = number, maxA
            
            elif number > maxB:
                
                maxB = number
                
        return (maxA - 1) * (maxB - 1)
                
        
        