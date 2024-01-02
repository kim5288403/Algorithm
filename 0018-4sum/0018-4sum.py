class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = set()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, h = j + 1, len(nums) - 1
            
                while(l < h):

                    four_sum = nums[i] + nums[j] + nums[l] + nums[h]

                    if four_sum < target:
                        l += 1
                    elif four_sum > target:
                        h -= 1
                    else:
                        result.add((nums[i], nums[j], nums[l], nums[h]))
                        l, h = l + 1, h - 1
        
        return result
        