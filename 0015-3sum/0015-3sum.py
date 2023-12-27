class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for i in range(len(nums) - 2):
            l, h = i + 1, len(nums) - 1
            
            while(l < h):
                three_sum = nums[i] + nums[l] + nums[h]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    h -= 1
                else:
                    result.add((nums[i], nums[l], nums[h]))
                    l, h = l + 1, h - 1
                
        
        
        
        return list(result)
        