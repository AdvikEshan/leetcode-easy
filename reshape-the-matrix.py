class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        myList = [x for row in nums for x in row ]
        
        if r * c == len(myList):
            return [myList[i*c:(i+1)*c] for i in range(r)]
        else:
            return nums
