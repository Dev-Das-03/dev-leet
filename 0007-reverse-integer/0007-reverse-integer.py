class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        c = 1

        if x < 0:
            x = abs(x)
            c = -1

        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10

        if ((ans * c) > 2147483647) or ((ans * c) < -2147483648):
            return 0
        else:
            return ans * c