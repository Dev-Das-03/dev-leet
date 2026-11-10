class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans = 0
        i = 0
        j = len(grid[0]) - 1
        while (i < len(grid) and j >= 0):
            if grid[i][j] < 0:
                ans += len(grid) - i
                j -= 1
            else:
                i += 1
        return ans