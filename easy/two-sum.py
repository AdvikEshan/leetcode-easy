class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1st solution
        # for i in range(0,len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]+nums[j] == target and j!=i:
        #             return [i,j]
        
        ## 2nd Solution
        for index, number in enumerate(nums):
            make_positive = target - number
            if (make_positive in nums) and (nums.index(make_positive) != index):
                return nums.index(make_positive), index
