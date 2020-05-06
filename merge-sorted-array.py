class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:len(nums1)]
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()     
#         i = j = 0
#         del nums1[m:len(nums1)]
#         while i < m and j < n:
#             if nums1[i] < nums2[j]:
#                 nums1[i]=nums1[i]
#                 i += 1
#             else:
#                 i += 1
#                 nums1.insert(i,nums2[j])
#                 j += 1
        
#         while j < n:
#             nums1.append(nums2[j])
#             j += 1
            
#         return nums1 

        # nums1[m:]=nums2
        # return nums1.sort()
            
