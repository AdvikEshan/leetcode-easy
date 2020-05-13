class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1st approach ->
        # Time-limit will exceed for long input list
        
        # length = len(nums)
        # nums = list(dict.fromkeys(nums))
        # for i in range(1,length+1):
        #     if i in nums:
        #         nums.remove(i)
        #     else:
        #         nums.append(i)
        # return nums
        
        return list((set(range(1, len(nums) + 1))) - (set(nums)))
