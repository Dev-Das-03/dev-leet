class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while n >= 3**i:
            if 3**i == n:
                return True
            i += 1
        return False 