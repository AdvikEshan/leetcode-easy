class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if(x < 0):
            x = x * -1
            negative = True
        else:
            x = x
        sum = 0
        count = 1
        
        strX = str(x)
        lst = list(strX)
        
        for i in lst:
            sum += int(i) * count
            count *= 10

        if(abs(sum) > (2 ** 31 - 1)):
            return 0
        elif(negative == True):
            return sum * -1
        else:
            return sum
