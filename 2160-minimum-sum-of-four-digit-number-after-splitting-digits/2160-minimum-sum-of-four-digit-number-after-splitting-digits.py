class Solution:
    def minimumSum(self, num: int) -> int:
        n2 = []
        s1,s2 = 0,0
        n1 = list(map(int,str(num)))
        n2.append(min(n1))
        n1.remove(min(n1))
        n2.append(max(n1))
        n1.remove(max(n1))
        n1.sort()
        for i in range(2):
            s1 = s1 * 10 + n1[i]
            s2 = s2 * 10 + n2[i]
        return s1 + s2

        