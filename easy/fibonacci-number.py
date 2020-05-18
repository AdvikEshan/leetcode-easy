class Solution:
    def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         return self.fib(N-1) + self.fib(N-2)
    
        a,b = 0,1
        for _ in range(N):
            a, b = b, a+b
        return a
