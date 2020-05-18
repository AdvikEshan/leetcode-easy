class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numsStr = ''.join(str(e) for e in digits)
        number = int(numsStr)+1
        return [int(x) for x in str(number)]
