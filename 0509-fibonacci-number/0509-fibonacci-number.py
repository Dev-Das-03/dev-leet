class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        t1,t2 = 0,1
        for i in range(n-1):
            t = t1 + t2
            t1,t2 = t2,t
        return t2