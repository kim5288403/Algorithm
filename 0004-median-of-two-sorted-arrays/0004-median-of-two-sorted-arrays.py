class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        
        l, r = 0, len(arr) - 1
        
        print(len(arr))
        
        
        while l <= r:
            if l == r:
                return arr[l]
            
            l += 1
            r -= 1
        
        return (arr[l] + arr[r]) / 2