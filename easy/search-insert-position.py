class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This one is better -> time complexity
        
        # if target in nums:
        #     return nums.index(target)
        # elif target > nums[len(nums)-1]:
        #     return len(nums)
        # else:
        #     for i in range(len(nums)):
        #         if nums[i]>target: 
        #             return nums.index(nums[i])
        
        for index,item in enumerate(nums):
            if item >= target:
                return index
            continue
        return len(nums)
