class Solution:
    def reverseBits(self, n: int) -> int:
        b = ""
        ans = 0
        while n > 0:
            b = f"{n % 2}" + b
            n //= 2
        b = (32 - len(b)) * "0" + b
        for i in range(len(b)):
            ans += (2**i) * int(b[i])
        return ans