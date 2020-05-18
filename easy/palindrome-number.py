class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse=0
            num = x
            while num:
                reverse = (reverse*10)+num%10
                num = num//10
            return True if reverse==x else False

# 1st Solution
#         if x < 0:
#             return False
#         else:
#             numStr = str(x)
#             numList = list(numStr)
#             reverseList = []    
            
#             for i in range(0,len(numList)):
#                 reverseList.append(numList.pop())
#             num = int(''.join(map(str,reverseList))) 
            
        
#         return True if num == x else False
