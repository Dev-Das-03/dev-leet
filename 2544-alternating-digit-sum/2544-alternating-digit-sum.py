class Solution:
    def alternateDigitSum(self, n: int) -> int:
        arr = str(n)
        ds,s = 0,1
        for i in range(len(arr)):
            ds += int(arr[i]) * s
            s *= -1
        return ds