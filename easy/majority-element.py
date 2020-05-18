class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)//2
# Time limit will exceed in case of long arrays [5k elements]
#         majority = 0
#         element = 0
        
#         for i in nums:
#             numCount = nums.count(i)
#             if numCount > length and numCount > majority: 
#                 majority = numCount
#                 element = i
#         return element

# Best solution
        # nums.sort()
        # element = nums[length]
        # return element

#         if not nums:
#             return None

# Boyce-Moore algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
