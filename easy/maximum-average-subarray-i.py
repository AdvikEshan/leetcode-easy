class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k: return sum(nums)/k
        
        # result = 0
        # for i in range(len(nums)-k+1):
        #     total = sum(nums[i:i+k])
        #     result = max(result,total)
        # return result/k
        
        sums=0
        sums=sum(nums[:k])
        res=sums
        for i in range(k,len(nums)):
            sums+=(nums[i]-nums[i-k])
            if res<sums:
                res=sums
        return res/k
