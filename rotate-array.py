class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        element = None
        # i = 0
        # while i < k:
        #     element = nums.pop()
        #     nums.insert(0,element)
        #     i += 1
        
        # length = len(nums)
        # for i in range(k):
        #     element = nums[-1]
        #     del nums[-1]
        #     nums.insert(0,element) 
        
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] 
            
