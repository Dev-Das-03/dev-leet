class Solution:
    def bi(self,a):
        b = 0
        i = 0
        while a > 0:
            dig = a % 2
            b = dig * (10**i) + b
            i += 1 
            a //= 2
        return b
    def dig(self,a):
        b = 0
        while a > 0:
            b += a % 10
            a //= 10
        return b  
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.dig(self.bi(i)))
        return ans