class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = ""
        c = 0
        while n > 0:
            bi = f"{n % 2}" + bi
            n = n // 2
        for i in range(len(bi)):
            if bi[i] == "1":
                c += 1
        return c