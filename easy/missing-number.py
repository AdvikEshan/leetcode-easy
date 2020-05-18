class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=[]
        for k in range(0,len(nums)+1):
            a.append(k)
        return sum(a)-sum(nums)
