class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        longest = temp = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
                longest = max(temp,longest)
            else: 
                temp = 1
        return longest`