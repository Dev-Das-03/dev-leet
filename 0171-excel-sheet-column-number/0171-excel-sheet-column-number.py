class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(1,len(columnTitle)+1):
            ans += (26 ** (i-1)) * (ord(columnTitle[-i]) - 64)
        return ans