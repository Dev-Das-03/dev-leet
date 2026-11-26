class Solution:
    def canAliceWin(self, n: int) -> bool:
        c,v = 0,10
        while n >= 0:
            if n < v:
                if c % 2 == 0:
                    return False
                else:
                    return True
            c += 1
            n -= v
            v -= 1