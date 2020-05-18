class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        median = abs(len(nums1) / 2)
        if len(nums1) % 2 == 0:
            return (nums1[int(median)] + nums1[int(median-1)]) / 2
        return nums1[int(median)]
    
# 1st solution
#         nums3 = nums1 + nums2
#         nums3.sort()
    
#         if len(nums3) %2 == 1:
#             return nums3[((len(nums3)+1)//2)-1]
#         else:
#             return (nums3[(len(nums3)//2)-1]+nums3[(len(nums3)+1)//2])/2
        
            
