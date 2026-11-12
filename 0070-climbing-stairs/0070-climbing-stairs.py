class Solution:
    def climbStairs(self, n: int) -> int:
        t1,t2 = 0,1
        for i in range(n):
            temp = t1 + t2
            t1,t2 = t2,temp
        return t2